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

from Volume import Volume
from SampleSpecification import SampleSpecification
from ChannelMap import ChannelMap
import Port

class Sink():
    def __init__(self, sink):
        self._as_parameter_ = int(sink.index)
        
        self.name = sink.name
        self.index = int(sink.index)
        self.description = sink.description
        self.sampleSpecification = SampleSpecification(sink.sample_spec)
        self.channelMap = ChannelMap(sink.channel_map)
        self.ownerModule = int(sink.owner_module)
        
        self.volume = Volume(sink.volume) # does this work?
        #self.volume = sink.volume.channels
        #for v in sink.volume.values:
        #    self.volume.append(v)
        
        self.mute = int(sink.mute)
        self.monitorSource = sink.monitor_source
        self.monitorSource_name = sink.monitor_source_name
        self.latency = sink.latency # class this
        self.driver = sink.driver
        self.flags = sink.flags # class this
        self.proplist = sink.proplist # class this
        self.configuredLatency = sink.configured_latency # class this
        self.baseVolume = int(sink.base_volume) # enum
        self.state = sink.state # class this
        self.nVolumeSteps = int(sink.n_volume_steps)
        self.card = int(sink.card)
        
#        self.ports = sink.ports # class this
#        self.ports = []
#        print sink.n_ports
#        for i in range(0, sink.n_ports):
#            print i
#            port = self.ports[i]
#            if port:
#                self.ports.insert(i, Port.SinkPort())
        
#        print sink.active_port
#        if sink.active_port:
#            print sink.active_port.contents
#            self.activePort = Port.SinkPort(sink.active_port.contents)