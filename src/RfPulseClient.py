# RfPulseLib
#
# Copyright (C) 2011 by Rohde Fischer <rohdef@rohdef.dk> www.rohdef.dk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from RfPulseLib import *
import ctypes
from ctypes import *

from model.Server import Server
from model.Sink import Sink
from model.Source import Source
from model.Module import Module
from model.Client import Client
from model.Card import Card
from model.SinkInput import SinkInput
import time

class RfPulseClient():
    """Provides an relatively easy way of communicating with PulseAudio"""
    
    def __init__(self, contextName):
        self.name = contextName
        self._pa = getPa()
        
        self.events = {
            'contextNotify': [],
            'contextConnected': [],
            'contextConnectionFailed': [],
            'contextDisconnected': [],
            'sinkInfoList': [],
            'sourceInfoList': [],
            'serverInfo': [],
            'moduleInfoList': [],
            'clientInfoList': [],
            'cardInfoList': [],
            'sinkInputInfoList': [],
            }

        self._resetLists()
        
        self._initCallbacks()
    
    def connect(self):
        '''Connects to the pulseaudio server, identifying this client with the name from the constructor.'''
        self.mainLoop = self._pa.pa_threaded_mainloop_new()
        self.mainLoopApi = self._pa.pa_threaded_mainloop_get_api(self.mainLoop)
        self.context = self._pa.pa_context_new(self.mainLoopApi, self.name)
        
        self._contextNotifyCallbackType = contextNotifyCallbackType(self._contextStateCallback)
        self._pa.pa_context_set_state_callback(self.context, self._contextNotifyCallbackType, None)
        
        self._pa.pa_context_connect(self.context, None, 0, None)
        self._pa.pa_threaded_mainloop_start(self.mainLoop)
        
        self._resetLists()
        
    def _initCallbacks(self):
        self._sinkInfoListCallbackType = sinkInfoListCallbackType(self._sinkInfoListCallback)
        self._sourceInfoListCallbackType = sourceInfoListCallbackType(self._sourceInfoListCallback)
        self._serverInfoCallbackType = serverInfoCallbackType(self._serverInfoCallback)
        self._moduleInfoListCallbackType = moduleInfoListCallbackType(self._moduleInfoListCallback)
        self._clientInfoListCallbackType = clientInfoListCallbackType(self._clientInfoListCallback)
        self._cardInfoListCallbackType = cardInfoListCallbackType(self._cardInfoListCallback)
        self._sinkInputInfoListCallbackType = sinkInputInfoListCallbackType(self._sinkInputInfoListCallback)
    
    def _resetLists(self):
        self.sinks = []
        self.sinkIndexes = []
        
        self.sources = []
        self.server = None
        self.modules = []
        self.clients = []
        self.cards = []
        self.sinkInputs = []
    
    def disconnect(self):
        self._pa.pa_context_disconnect(self.context)
        self._pa.pa_context_unref(self.context)
        
        # These seems to cause trouble, problem is, afaik they should be there
        self._pa.pa_threaded_mainloop_stop(self.mainLoop)
        self._pa.pa_threaded_mainloop_free(self.mainLoop)
        self._resetLists()

    def getSinkInfoList(self):
        operation = self._pa.pa_context_get_sink_info_list(self.context,
            self._sinkInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)

    def _sinkInfoListCallback(self, context, sinkInfo, eol, userData):
        if sinkInfo:
            sink = Sink(sinkInfo.contents)
            self.sinks.insert(sink.index, sink)
            self.sinkIndexes.append(sink.index)
            
            for ev in self.events['sinkInfoList']:
                ev(userData)
    
    def getSourceInfoList(self):
        operation = self._pa.pa_context_get_source_info_list(self.context,
            self._sourceInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _sourceInfoListCallback(self, context, sourceInfo, eol, userData):
        if sourceInfo:
            source = Source(sourceInfo.contents)
            self.sources.insert(source.index, source)
            
            for ev in self.events['sourceInfoList']:
                ev(userData)
    
    def getServerInfo(self):
        operation = self._pa.pa_context_get_server_info(self.context, self._serverInfoCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _serverInfoCallback(self, context, serverInfo, userData):
        if serverInfo:
            self.server = Server(serverInfo.contents)
            
            for ev in self.events['serverInfo']:
                ev(userData)
    
    def getModuleInfoList(self):
        operation = self._pa.pa_context_get_module_info_list(self.context, self._moduleInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _moduleInfoListCallback(self, context, moduleInfo, eol, userData):
        if moduleInfo:
            module = Module(moduleInfo.contents)
            self.modules.insert(module.index, module)
            
            for ev in self.events['moduleInfoList']:
                ev(userData)
    
    def getClientInfoList(self):
        operation = self._pa.pa_context_get_client_info_list(self.context, self._clientInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _clientInfoListCallback(self, context, clientInfo, eol, userData):
        if clientInfo:
            client = Client(clientInfo.contents)
            self.clients.insert(client.index, client)
            
            for ev in self.events['clientInfoList']:
                ev(userData)
    
    def getCardInfoList(self):
        operation = self._pa.pa_context_get_card_info_list(self.context, self._cardInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _cardInfoListCallback(self, context, cardInfo, eol, userData):
        if cardInfo:
            card = Card(cardInfo.contents)
            self.cards.insert(card.index, card)
            
            for ev in self.events['cardInfoList']:
                ev(userData)
    
    def getSinkInputInfoList(self):
        operation = self._pa.pa_context_get_sink_input_info_list(self.context, self._sinkInputInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)
    
    def _sinkInputInfoListCallback(self, context, sinkInputInfo, eol, userData):
        if sinkInputInfo:
            sinkInput = SinkInput(sinkInputInfo.contents)
            self.sinkInputs.insert(sinkInput.index, sinkInput)
            
            for ev in self.events['sinkInputInfoList']:
                ev(userData)
    
    
    
    def _contextStateCallback(self, context, userData):
        state = self._pa.pa_context_get_state(context)
        
        if  state == ContextState.READY:
            for ev in self.events['contextConnected']:
                ev(userData)
        elif state == ContextState.FAILED:
            for ev in self.events['contextConnectionFailed']:
           	    pass
        elif state == ContextState.TERMINATED:
            for ev in self.events['contextDisconnected']:
                pass    
    
    def _sinkListCallback(self, context, sink_info, eol, userData):
        for ev in self.events['sinkInfoList']:
            #ev(userData)
            pass
