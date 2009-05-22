# Virtualkey - wrapper for python-virtkey
# Depends on python-virtkey
# Copyright (c) 2009. Krunoslav Husak, http://h00s.net, kruno@binel.hr

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import virtkey

class VirtualKey:

    def __init__(self):
        self.key_emulator = virtkey.virtkey()
        self.keys = { 'lctrl':0xffe3, 'xf86audioplay':0x1008ff14 }
        self.toggled_keys = []

    def get_key_code(self, key):
        if type(key) == type(""):
            if self.keys.has_key(key):
                return self.keys[key]
            else:
                return ord(key)

    def convert_key(self, key_codes):
        if type(key_codes) == type([]):
            for index, key_code in enumerate(key_codes):
                key_codes[index] = self.get_key_code(key_code)
            return key_codes
        else:
            return self.get_key_code(key_codes)

    def hold_key(self, key_codes):
        key_codes = self.convert_key(key_codes)
        if type(key_codes) == type([]):
            for key_code in key_codes:
                self.key_emulator.press_keysym(key_code)
        else:
            print key_codes
            self.key_emulator.press_keysym(key_codes)

    def release_key(self, key_codes):
        key_codes = self.convert_key(key_codes)
        if type(key_codes) == type([]):
            for key_code in reversed(key_codes):
                self.key_emulator.release_keysym(key_code)
        else:
            self.key_emulator.release_keysym(key_codes)

    def press_key(self, key_codes):
        self.hold_key(key_codes)
        self.release_key(key_codes)
