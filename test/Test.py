#!/usr/bin/python

import time
import unittest
import sys
sys.path.insert(1, '../src')
from RfPulseClient import RfPulseClient
from model.Volume import Volume
from model.SampleSpecification import SampleSpecification
from model.ChannelMap import ChannelMap
import model.Port

Port = model.Port

class TestRfPulseClient(unittest.TestCase):
    def setUp(self):
        self.h = _H()
        self.pa = RfPulseClient("RfPulseClient unit test")
        self.pa.connect()
        time.sleep(1)
    
    def tearDown(self):
        self.pa.disconnect()
    
    
    ############# 
    # TEST CASES
    #############
      
    def testSinks(self):
        self.pa.getSinkInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sinks) > 0,
            'There is no sinks present')
        
        for s in self.pa.sinks:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            self.h.sinkSourceTest(self, s)
            
            # state
            # Flags
    
    def testSources(self):
        self.pa.getSourceInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sources) > 0,
            'There is no sources present')
        
        for s in self.pa.sources:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            self.h.sinkSourceTest(self, s)
            # state
            # Flags
    
    def testServerInfo(self):
        self.pa.getServerInfo()
        time.sleep(1)
        
        s = self.pa.server
        self.assertTrue(isinstance(s.hostName, basestring))
        self.assertTrue(isinstance(s.serverName, basestring))
    
    def testModules(self):
        self.pa.getModuleInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.modules) > 0,
            'No modules presen')
        
        for m in self.pa.modules:
            self.h.generalModel(self, m)
            self.h.propTest(self, m)
    
    def testClients(self):
        self.pa.getClientInfoList()
        time.sleep(1)
        
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
        self.pa.getCardInfoList()
        time.sleep(1)
        
        self.assertTrue(self.pa.cards > 0,
            'No cards present')
        
        for c in self.pa.cards:
            self.h.generalModel(self, c)
            self.h.propDriverAndOwnerTest(self, c)
    
    def testSinkInputs(self):
        self.pa.getSinkInputInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sinkInputs) > 0, "There is no sink inputs")
        
        for s in self.pa.sinkInputs:
            self.h.generalModel(self, s)
            self.h.volumeTest(self, s)
            # self.h.propDriverAndOwnerTest(self, s)
            # TODO fix segfault with driver for sinkinputs
    


class _H():
    '''This a helper class for the tests for reusing common test cases.'''
        
    def generalModel(self, t, model):
        '''Tests the general parts of nearly all model classes'''
        
        t.assertTrue(isinstance(model.name, basestring))
        t.assertTrue(model.index > -1)
    
    def volumeTest(self, t, model):
        '''Tests the classes with volume and the related properties.'''
        
        # Volume
        
        t.assertTrue(isinstance(model.volume, Volume))
        # t.assertTrue(model.volume.channels > 0) # can I even assume this?
        t.assertEquals(model.volume.channels, len(model.volume.values))
        
        for c in model.volume.values:
            t.assertTrue(c >= 0)
        
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
        activePort = model.activePort;
        t.assertIsInstance(activePort, Port._Port)
        
        # TODO not the case, is this a bug or is i possible?
        #t.assertIsInstance(activePort.name, basestring)
        #t.assertTrue(len(activePort.name) > 0)
        
        #t.assertIsInstance(activePort.description, basestring)
        #t.assertTrue(len(activePort.description) > 0)
        
        t.assertIsInstance(activePort.priority, int)
        t.assertTrue(activePort.priority > -1)
        
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
