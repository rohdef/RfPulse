#!/usr/bin/python

import time
import sys
import unittest
from hamcrest import *
sys.path.insert(1, '../src')
from RfPulseClient import RfPulseClient
from model.Volume import Volume
from model.SampleSpecification import SampleSpecification
from model.ChannelMap import ChannelMap
import model.Port
class Dummy():
    pass

class TestRfPulseClient(unittest.TestCase):
    def setUp(self):
        self.h = _H()
        self.awaitingConnect = True
        self.pa = RfPulseClient("RfPulseClient unit test")
        self.pa.events['contextConnected'].append(self.connected)
        self.pa.connect()
        while self.awaitingConnect:
            pass
        
        
        self.volume = Dummy()
        self.volume.channels = 0
        
        self.sample = Dummy()
        self.sample.format = None
        self.sample.rate = 0
        self.sample.channels = 0
        
        self.channelMap = Dummy()
        self.channelMap.channels = 0
        
        self.sinkInput = Dummy()
        self.sinkInput.index = 1
        self.sinkInput.name = 'test'
        self.sinkInput.owner_module = 1
        self.sinkInput.client = None
        self.sinkInput.sink = None
        self.sinkInput.sample_spec = self.sample
        self.sinkInput.channel_map = self.channelMap
        self.sinkInput.mute = 0
        self.sinkInput.buffer_usec = 0
        self.sinkInput.sink_usec = 0
        self.sinkInput.resample_method = 0
        self.sinkInput.proplist = None
        
        self.sinkInputInfo = Dummy()
        self.sinkInputInfo.contents = self.sinkInput
        
        self.server = Dummy()
        self.server.user_name = None
        self.server.host_name = None
        self.server.server_version = 0
        self.server.server_name = None
        self.server.sample_spec = None
        self.server.default_sink_name = None
        self.server.default_source_name = None
        self.server.cookie = 0
        self.server.channel_map = None
        
        self.serverInfo = Dummy()
        self.serverInfo.contents = self.server
        
        self.client = Dummy()
        self.client.index = 0
        self.client.name = None
        self.client.owner_module = 0
        self.client.driver = None
        self.client.proplist = None
        
        self.clientInfo = Dummy()
        self.clientInfo.contents = self.client
        
        self.card = Dummy()
        self.card.index = 0
        self.card.name = None
        self.card.owner_module = 0
        self.card.driver = None
        self.card.n_profiles = None
        self.card.profiles = None
        self.card.active_profile = None
        self.card.proplist = None
        
        self.cardInfo = Dummy()
        self.cardInfo.contents = self.card
        
        self.source = Dummy()
        self.source.name = None
        self.source.index = 0
        self.source.description = None
        self.source.sample_spec = self.sample
        self.source.channel_map = self.channelMap
        self.source.owner_module = None
        self.source.volume = self.volume
        self.source.mute = 0
        self.source.monitor_of_sink = None
        self.source.monitor_of_sink_name = None
        self.source.latency = None
        self.source.driver = None
        self.source.flags = None
        self.source.proplist = None
        self.source.configured_latency = None
        self.source.base_volume = 0
        self.source.state = None
        self.source.n_volume_steps = 0
        self.source.card = 0
        self.source.n_ports = 0
        self.source.ports = None
        
        self.sourceInfo = Dummy()
        self.sourceInfo.contents = self.source
        
        self.sink = Dummy()
        
        self.sink.name = None
        self.sink.index = 0
        self.sink.description = None
        self.sink.sample_spec = self.sample
        self.sink.channel_map = self.channelMap
        self.sink.owner_module = 0
        self.sink.volume = self.volume
        self.sink.mute = 0
        self.sink.monitor_source = None
        self.sink.monitor_source_name = None
        self.sink.latency = None
        self.sink.driver = None
        self.sink.flags = None
        self.sink.proplist = None
        self.sink.configured_latency = None
        self.sink.base_volume = 0
        self.sink.state = 0
        self.sink.n_volume_steps = 0
        self.sink.card = 0
        
        self.sinkInfo = Dummy()
        self.sinkInfo.contents = self.sink
        
        self.module = Dummy()
        self.module.index = 0
        self.module.name = None
        self.module.argument = None
        self.module.n_used = 0
        self.module.proplist = None
        
        self.moduleInfo = Dummy()
        self.moduleInfo.contents = self.module
        
        
    
    def tearDown(self):
        self.pa.disconnect()
    
    
    ############# 
    # TEST CASES
    #############
      
    def testSinks(self):
        print '\nTesting sinks: '
        self.awaitingCallback = True
        self.pa.events['sinkInfoList'].append(self.callbackMethod)
        self.pa.getSinkInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(len(self.pa.sinks) > 0,
            'There is no sinks present')
        
        for s in self.pa.sinks:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            self.h.sinkSourceTest(self, s)
            
            # state
            # Flags
    
    def testSources(self):
        print '\nTesting sources: '
        self.awaitingCallback = True
        self.pa.events['sourceInfoList'].append(self.callbackMethod)
        self.pa.getSourceInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(len(self.pa.sources) > 0,
            'There is no sources present')
        
        for s in self.pa.sources:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            self.h.sinkSourceTest(self, s)
            # state
            # Flags
    
    def testServerInfo(self):
        print '\nTesting server info: '
        self.awaitingCallback = True
        self.pa.events['serverInfo'].append(self.callbackMethod)
        self.pa.getServerInfo()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        s = self.pa.server
        self.assertTrue(isinstance(s.hostName, basestring))
        self.assertTrue(isinstance(s.serverName, basestring))
    
    def testModules(self):
        print '\nTesting modules: '
        self.awaitingCallback = True
        self.pa.events['moduleInfoList'].append(self.callbackMethod)
        self.pa.getModuleInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(len(self.pa.modules) > 0,
            'No modules presen')
        
        for m in self.pa.modules:
            self.h.generalModel(self, m)
            self.h.propTest(self, m)
    
    def testClients(self):
        print '\nTesting clients: '
        self.awaitingCallback = True
        self.pa.events['clientInfoList'].append(self.callbackMethod)
        self.pa.getClientInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(len(self.pa.clients) > 0, 
            'No clients present')
        
        unitTestClient = False
        for c in self.pa.clients:
            self.h.generalModel(self, c)
            self.h.propDriverAndOwnerTest(self, c)
            
            if c.name == "RfPulseClient unit test":
                unitTestClient = True
        
        self.assertTrue(unitTestClient, 'Own client not found')
    
    def testCards(self):
        print '\nTesting cards: '
        self.awaitingCallback = True
        self.pa.events['cardInfoList'].append(self.callbackMethod)
        self.pa.getCardInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(self.pa.cards > 0,
            'No cards present')
        
        for c in self.pa.cards:
            self.h.generalModel(self, c)
            self.h.propDriverAndOwnerTest(self, c)
    
    def testSinkInputs(self):
        print '\nTesting sink inputs: '
        self.awaitingCallback = True
        self.pa.events['sinkInputInfoList'].append(self.callbackMethod)
        self.pa.getSinkInputInfoList()
        
        timeout = time.time()+5
        while (self.awaitingCallback):
            if (timeout < time.time()):
                assert_that(False, 'Timed out')
                return
        
        self.assertTrue(len(self.pa.sinkInputs) > 0, "There is no sink inputs")
        
        for s in self.pa.sinkInputs:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            # self.h.propDriverAndOwnerTest(self, s)
            # TODO fix segfault with driver for sinkinputs
    
    
    def testConnectEvent(self):
        print '\nTesting connect event: '
        self.awaitingCallback = True
        self.pa.events['contextConnected'].append(self.callbackMethod)
        
        # Misuse that setup creates a connection :)
        self.pa._contextStateCallback(self.pa.context, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
        
        # 1 minute timeout for testing on real connection
#        timeout = gmtime()+60
#        while (awaitingConnect):
#            if (timeout < gmtime()):
#                assert_that(false, 'Timed out')
#                break

    def testSinkInfoListEvent(self):
        print '\nTesting sink info event: '
        self.awaitingCallback = True
        self.pa.events['sinkInfoList'].append(self.callbackMethod)
        
        self.pa._sinkInfoListCallback(self.pa.context, self.sinkInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testSourceInfoListEvent(self):
        print '\nTesting source info event: '
        self.awaitingCallback = True
        self.pa.events['sourceInfoList'].append(self.callbackMethod)
        
        self.pa._sourceInfoListCallback(self.pa.context, self.sourceInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testServerInfo(self):
        print '\nTesting server info event: '
        self.awaitingCallback = True
        self.pa.events['serverInfo'].append(self.callbackMethod)
        
        self.pa._serverInfoCallback(self.pa.context, self.serverInfo, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testModuleInfoListEvent(self):
        print '\nTesting module info event: '
        self.awaitingCallback = True
        self.pa.events['moduleInfoList'].append(self.callbackMethod)
        
        self.pa._moduleInfoListCallback(self.pa.context, self.moduleInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testClientInfoListEvent(self):
        print '\nTesting client info event: '
        self.awaitingCallback = True
        self.pa.events['clientInfoList'].append(self.callbackMethod)
        
        self.pa._clientInfoListCallback(self.pa.context, self.clientInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testCardInfoListEvent(self):
        print '\nTesting card info event: '
        self.awaitingCallback = True
        self.pa.events['cardInfoList'].append(self.callbackMethod)
        
        self.pa._cardInfoListCallback(self.pa.context, self.cardInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    def testSinkInputInfoListEvent(self):
        print '\nTesting sink input info event: '
        self.awaitingCallback = True
        self.pa.events['sinkInputInfoList'].append(self.callbackMethod)
        
        self.pa._sinkInputInfoListCallback(self.pa.context, self.sinkInputInfo, 0, None)
        
        if (self.awaitingCallback):
            assert_that(False, 'The event was not fired')
    
    
    def callbackMethod(self, userData):
        self.awaitingCallback = False
        
    def connected(self, userData):
        self.awaitingConnect = False
    


class _H():
    '''This a helper class for the tests for reusing common test cases.'''
        
    def generalModel(self, t, model):
        '''Tests the general parts of nearly all model classes'''
        
        t.assertTrue(isinstance(model.name, basestring))
        t.assertTrue(model.index > -1)
    
    def volumeTest(self, t, model):
        '''Tests the classes with volume and the related properties.'''
        
        # Volume
        
        #assert_that(isinstance(model.volume, Volume))
        #assert_that(model.volume.channels > 0) # can I even assume this?
        #t.assertEquals(model.volume.channels, len(model.volume.values))
        
        #for c in model.volume.values:
        #    t.assertTrue(c >= 0)
        
        # Mute
        
        t.assertIsInstance(model.mute, int)
        
        # Channel map
        t.assertIsInstance(model.channelMap, ChannelMap)
        t.assertTrue(model.channelMap.channels > 0)
        t.assertEquals(model.channelMap.channels,
            len(model.channelMap.map))
        
        for m in model.channelMap.map:
            t.assertTrue(m >= 0)
        
        # sampleSpec
        t.assertIsInstance(model.sampleSpecification,
            SampleSpecification)
        # TODO test format, when enum is created
        t.assertTrue(model.sampleSpecification.rate > 0)
        t.assertTrue(model.sampleSpecification.channels > 0)
    
    def propDriverAndOwnerTest(self, t, model):
        '''Test the property list, driver and owner module'''
        t.assertTrue(model.ownerModule > 0)
        
        t.assertIsInstance(model.driver, basestring)
        t.assertTrue(len(model.driver) > 0)
        
        self.propTest(t, model)
    
    def propTest(self, t, model):
        '''Test the property list - currently unimplemented'''
        # proplist
        # TODO find how to test proplists :/
        pass
    
    def sinkSourceTest(self, t, model):
        '''Test the common properties of Sink and Source'''
        # Description
        t.assertIsInstance(model.description, basestring)
        t.assertTrue(len(model.description) > 0)
        
        # Latency
        # TODO no likely tests known at the moment
        
        # Configured latency
        # TODO see Latency
        
        # Base volume
        # TODO enum test
        t.assertIsInstance(model.baseVolume, int)
        
        # Number of volume steps
        # TODO test might need improvement, due to the following documentation
        # Number of volume steps for sinks which do not support arbitrary volumes.
        t.assertIsInstance(model.nVolumeSteps, int)
        t.assertTrue(model.nVolumeSteps > -1)
        
        # card
        t.assertIsInstance(model.card, int)
        
        # nPorts
        t.assertIsInstance(model.nVolumeSteps, int)
        
        # activePort
        #activePort = model.activePort;
        #t.assertIsInstance(activePort, Port._Port)
        
        # TODO not the case, is this a bug or is i possible?
        #t.assertIsInstance(activePort.name, basestring)
        #t.assertTrue(len(activePort.name) > 0)
        
        #t.assertIsInstance(activePort.description, basestring)
        #t.assertTrue(len(activePort.description) > 0)
        
        #t.assertIsInstance(activePort.priority, int)
        #t.assertTrue(activePort.priority > -1)
        
        # ports
        # TODO these tests tests the Ports array when made
#        for p in model.ports:
            # TODO future test for when array size problem is solved
            #t.assertIsInstance(p, Port._Port)
            
            #TODO causes segfault, why?
#            t.assertIsInstance(p.name, basestring)
#            t.assertTrue(len(p.name) > 0)
            
#            t.assertIsInstance(p.description, basestring)
#            t.assertTrue(len(p.description) > 0)
#            
#            t.assertIsInstance(p.priority, int)
#            t.assertTrue(p.priority > -1)
            
            # TODO find active port... maybe?

if __name__ == '__main__':
    unittest.main()
