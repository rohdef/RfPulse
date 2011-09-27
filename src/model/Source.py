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

class Source():
    def __init__(self, source):
        self.name = source.name
        self.index = int(source.index)
        self.description = source.description
        self.sampleSpecification = SampleSpecification(source.sample_spec)
        self.channelMap = ChannelMap(source.channel_map)
        self.ownerModule = source.owner_module
        self.volume = Volume(source.volume) # does this work?
        self.mute = int(source.mute)
        self.monitorOfSink = source.monitor_of_sink
        self.monitorOfSink_name = source.monitor_of_sink_name
        self.latency = source.latency # class
        self.driver = source.driver
        self.flags = source.flags # class
        self.proplist = source.proplist # class
        self.configured_latency = source.configured_latency # class
        self.baseVolume = int(source.base_volume) # class
        self.state = source.state # class
        self.nVolumeSteps = int(source.n_volume_steps)
        self.card = int(source.card)
        self.nPorts = int(source.n_ports)
        self.ports = source.ports # class
        self.activePort = Port.SourcePort(source.active_port) # class