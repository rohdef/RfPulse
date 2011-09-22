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


class Server():
    def __init__(self, server):
        self.userName = server.user_name
        self.hostName = server.host_name
        self.serverVersion = server.server_version
        self.serverName = server.server_name
        self.sampleSpec = server.sample_spec # this should have a class
        self.defaultSinkName = server.default_sink_name
        self.defaultSourceName = server.default_source_name
        self.cookie = int(server.cookie)
        self.channelMap = server.channel_map # this should have a class