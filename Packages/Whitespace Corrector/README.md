#About

Whitespace Corrector is a plugin for [Sublime Text 2][1] that allows replace spaces with given length by tabulations and removes trailing whitespaces


##Install

If your using the [Sublime Package Manger][2] hold down Ctrl+shift+p and type
`Package Control: Install Package`. Then search for `whitespacecorrector` and hit return.

If your not using the package manager then `cd` into your Sublime packages directory. (On Linux this is ~/Sublime Text 2/Packages) Then run this command `hg clone https://bitbucket.org/homura/Whitespacecorrector`.

Or you can download the package as a zip file [https://bitbucket.org/homura/Whitespacecorrector/get/tip.zip][3] then copy it into your Sublime packages directory.

##Usage

Open context menu (by clicking right mouse button), then click to "Whitespacecorrector" item

You can also bind to key at Preferences -> Key bindings - User 
and insert line given below
{ "keys": ["ctrl+shift+t"], "command": "whitespacecorrector" }


![enter image description here][4]


# Source Code
http://bitbicket.org/homura/whitespacecorrector

# License

Whitespace Corrector is released under the MIT license.

Copyright (c) 2011 Zhomart <mzhomart@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Version 0.1
- Initial release



  [1]: http://www.sublimetext.com/2
  [2]: http://wbond.net/sublime_packages/package_control
  [3]: https://bitbucket.org/homura/Whitespacecorrector/get/tip.zip
  [4]: http://bitbucket.org/
