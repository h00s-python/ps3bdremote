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
        self.keys = { 'ctrl_left':0xffe3, 'super_left':0xffeb, 'alt_left':0xffe9, 'alt_gr':0xfe03, 'super_right':0xffec, 'ctrl_right':0xffe4,
                    'shift_left':0xffe1, 'shift_right':0xffe2, 'caps_lock':0xffe5, 'enter':0xff0d, 'tab':0xff09, 'backspace':0xff08,
                    'esc':0xff1b, 'f1':0xffbe, 'f2':0xffbf, 'f3':0xffc0, 'f4':0xffc1, 'f5':0xffc2, 'f6':0xffc3, 'f7':0xffc4, 'f8':0xffc5, 'f9':0xffc6, 'f10':0xffc7, 'f11':0xffc8, 'f12':0xffc9,
                    'scroll_lock':0xff14, 'pause':0xff13, 'insert':0xff63, 'home':0xff50, 'page_up':0xff55, 'delete':0xffff, 'end':0xff57, 'page_down':0xff56,
                    'arrow_up':0xff52, 'arrow_down':0xff54, 'arrow_left':0xff51, 'arrow_right':0xff53, 'num_lock':0xff63,
                    'num_divide':0xffaf, 'num_multiply':0xffaa, 'num_subtract':0xffad, 'num_add':0xffab, 'num_enter':0xff8d, 'num_0':0xffb0, 'num_1':0xffb1, 'num_2':0xffb2, 'num_3':0xffb3,
                    'num_4':0xffb4, 'num_5':0xffb5, 'num_6':0xffb6, 'num_7':0xffb7, 'num_8':0xffb8, 'num_9':0xffb9, 'num_separator':0xffac }
        self.toggled_keys = []

    def get_key_code(self, key):
        key = key.lower
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
