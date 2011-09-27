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

class SinkInput():
    def __init__(self, sinkInput):
        self.index = sinkInput.index
        self.name = sinkInput.name
        self.ownerModule = int(sinkInput.owner_module)
        self.client = sinkInput.client
        self.sink = sinkInput.sink
        self.sampleSpecification = SampleSpecification(sinkInput.sample_spec)
        self.channelMap = ChannelMap(sinkInput.channel_map)
        self.volume = Volume(sinkInput.volume) # does this work?
        self.mute = int(sinkInput.mute)
        self.bufferUsec = sinkInput.buffer_usec # enum
        self.sinkUsec = sinkInput.sink_usec # enum
        self.resampleMethod = sinkInput.resample_method
        #self.driver = sinkInput.driver # TODO causes segfault, will be fixed later
        self.proplist = sinkInput.proplist # class this
