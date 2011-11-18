#RfPulse
RfPulse is the aim to create a useful library for using PulseAudio in Python.
Basically because I could not find a proper library for this.

#Project organization

The project is divided into two parts:

+ RfPulseClient Which aims to be an easy to use client, and lies on top of the low level library. The target of this is that developers won't have to worry about the low level details.
	
+ RfPulseLib The library which makes all the low level PulseAudio calls accessible for Python. Since the lib and client is at such a early stage, this is needed to create any somewhat useful code.



#Usage
At the moment you can't do much with the library. But the basic usage is as follows:

    from RfPulseClient import RfPulseClient
    
    def connected():
        pass
    
    def sinkInfoListReturned():
        pass
    
    # The connection name will usually be the name of your app
    pa = RfPulseClient("Connection name")
    pa.connect()
    pa.getSinkInfoList()
    sink = pa.sinks[0]
    print sink.description
    pa.disconnect()


#Contact
##Bugs, feature requests etc.
Currently I would as people from refraining to reporting bugs, since this
project is in such an early stage.

I would also prefer that I get no feature requests at the moment. Most likely they would just be ignored, since my priority is to get the basics to work first.

If you have suggestions for improvement of code (read pattern suggestions, better ways of solving problems etc.) I would be happy to get your requests.

## Support
Currently most support does not make sense.

If you feel that there is some knowledge that would be nice to see shared, please feel free to write on the [wiki on github](https://github.com/rohdef/RfPulse/wiki).

Conditions for getting support from me personally are:

1. Don't ask before reading the entire readme (no offence, but it's short)
2. Don't call me directly.
3. Be as specific as possible.
4. Examples and/or unit tests that shows what's happening is appreciated.
5. No support is given without a funny picture, preferrable including yourself, a goat and a glass of water.
6. Please keep in mind that this project is no where near finished.

## Contact details
Also if you feel like you can help out in any other way feel free to contact me :)

    Rohde Fischer
    Kirkegaardsvej 10 D, 3.-3
    DK-8000 Aarhus C
    Denmark
    <rohdef@rohdef.dk>



#Thanks to
+ Alex Holkner for developing a ctypes library loader originally used for [pyglet](http://www.pyglet.org/) especially thanks for the choise of the BSD license.
+ The [PulseAudio](http://www.pulseaudio.org/) team for providing the best sound server I tried and for providing the APIs needed for this project.
+ Eric from [ypass.net](http://ypass.net) for providing an PulseAudio code example to get me started



#License (yes, boring part, at least it's short)
Copyright (C) 2011 by Rohde Fischer <rohdef@rohdef.dk> [rohdef.dk](http://rohdef.dk)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.