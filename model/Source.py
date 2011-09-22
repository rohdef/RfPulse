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

class Source():
    def __init__(self, source):
        self.name = output.name
        self.index = output.index
        self.description = output.description
        self.sample_spec = output.sample_spec # class
        self.channel_map = output.channel_map # class
        self.owner_module = output.owner_module
        self.volume = Volume(output.volume) # does this work?
        self.mute = output.mute
        self.monitor_of_sink = output.monitor_of_sink
        self.monitor_of_sink_name = output.monitor_of_sink_name
        self.latency = output.latency # class
        self.driver = output.driver
        self.flags = output.flags # class
        self.proplist = output.proplist # class
        self.configured_latency = output.configured_latency # class
        self.base_volume = output.base_volume # class
        self.state = output.state # class
        self.n_volume_steps = output.n_volume_steps
        self.card = output.card
        self.n_ports = output.n_ports
        self.ports = output.ports # class
        self.active_port = output.active_port # class