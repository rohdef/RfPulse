#!/usr/bin/python

import time
import unittest
import sys
sys.path.insert(1, '../src')
from RfPulseClient import RfPulseClient

class TestRfPulseClient(unittest.TestCase):
    def setUp(self):
        self.pa = RfPulseClient("RfPulseClient unit test")
        self.pa.connect()
        time.sleep(1)
    
    def tearDown(self):
        self.pa.disconnect()
    
  
      
    def testSinks(self):
        self.pa.getSinkInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sinks) > 0,
            'There is no sinks present')
        
        for s in self.pa.sinks:
            self.assertTrue(isinstance(s.name, basestring))
            self.assertTrue(s.index > -1)
    
    def testSources(self):
        self.pa.getSourceInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sources) > 0,
            'There is no sources present')
        
        for s in self.pa.sources:
            self.assertTrue(isinstance(s.name, basestring))
    
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
            self.assertTrue(isinstance(m.name, basestring))
            self.assertTrue(m.index > -1)
    
    def testClients(self):
        self.pa.getClientInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.clients) > 0, 
            'No clients present')
        
        unitTestClient = False
        for c in self.pa.clients:
            self.assertTrue(isinstance(c.name, basestring))
            self.assertTrue(c.index > -1)
            
            if c.name == "RfPulseClient unit test":
                unitTestClient = True
        
        self.assertTrue(unitTestClient, 'Own client not found')
    
    def testCards(self):
        self.pa.getCardInfoList()
        time.sleep(1)
        
        self.assertTrue(self.pa.cards > 0,
            'No cards present')
        
        for c in self.pa.cards:
            self.assertTrue(isinstance(c.name, basestring))
            self.assertTrue(c.index > -1)
    
    def testSinkInputs(self):
        self.pa.getSinkInputInfoList()
        time.sleep(1)
        
        self.assertTrue(len(self.pa.sinkInputs) > 0, "There is no sink inputs")
        
        for s in self.pa.sinkInputs:
            self.assertTrue(isinstance(s.name, basestring))
            self.assertTrue(s.index > -1)
    

if __name__ == '__main__':
    unittest.main()
