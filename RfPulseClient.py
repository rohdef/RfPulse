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


class RfPulseClient():
    """Provides an relatively easy way of communicating with PulseAudio"""
    
    def __init__(self, contextName):
        self.name = contextName
        self._pa = getPa()
    
    def connect(self):
        self.mainLoop = self._pa.pa_threaded_mainloop_new()
        self.mainLoopApi = self._pa.pa_threaded_mainloop_get_api(self.mainLoop)
        self.context = self._pa.pa_context_new(self.mainLoopApi, self.name)
        
        self._contextNotifyCallbackType = contextNotifyCallbackType(self._contextStateCallback)
        self._pa.pa_context_set_state_callback(self.context, self._contextNotifyCallbackType, None)
        
        self._pa.pa_context_connect(self.context, None, 0, None)
        self._pa.pa_threaded_mainloop_start(self.mainLoop)
        
        self.sinks = []
    
    def disconnect(self):
        self._pa.pa_context_disconnect(self.context)
        self._pa.pa_context_unref(self.context)
        
        # These seems to cause trouble, problem is, afaik they should be there
#        self._pa.pa_threaded_mainloop_stop()
#        self._pa.pa_threaded_mainloop_free()

    def getSinkInfoList(self):
        self._sinkInfoListCallbackType = sinkInfoCallbackType(self._sinkInfoListCallback)
        operation = self._pa.pa_context_get_sink_info_list(self.context, self._sinkInfoListCallbackType, None)
        self._pa.pa_operation_unref(operation)

    def _sinkInfoListCallback(self, context, sinkInfo, userData):
        if sinkInfo:
            self.sinks.append(sinkInfo.contents)
        # TODO event
    
    def _contextStateCallback(self, context, userData):
        #print 'Context state: {0}'.format(ContextState.states[self._pa.pa_context_get_state(context)])
        # TODO event
        
        state = self._pa.pa_context_get_state(context)
        
        if state == ContextState.UNCONNECTED:
            pass
        elif state == ContextState.CONNECTING:
            pass
        elif state == ContextState.AUTHORIZING:
            pass
        elif state == ContextState.SETTING_NAME:
            pass
        elif state == ContextState.READY:
            print 'Ready'
        elif state == ContextState.FAILED:
            pass
        elif state == ContextState.TERMINATED:
            pass
    
    def _sinkListCallback(self, context, sink_info, eol, userData):
        pass
