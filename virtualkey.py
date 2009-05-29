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
                    'num_4':0xffb4, 'num_5':0xffb5, 'num_6':0xffb6, 'num_7':0xffb7, 'num_8':0xffb8, 'num_9':0xffb9, 'num_separator':0xffac,
                    'xf86modelock':0x1008ff01, 'xf86monbrightnessup':0x1008ff02, 'xf86monbrightnessdown':0x1008ff03, 'xf86kbdlightonoff':0x1008ff04, 'xf86kbdbrightnessup':0x1008ff05, 'xf86kbdbrightnessdown':0x1008ff06,
                    'xf86standby':0x1008ff10, 'xf86audiolowervolume':0x1008ff11, 'xf86audiomute':0x1008ff12, 'xf86audioraisevolume':0x1008ff13, 'xf86audioplay':0x1008ff14, 'xf86audiostop':0x1008ff15,
                    'xf86modelock':0x1008ff01, 'xf86monbrightnessup':0x1008ff02, 'xf86monbrightnessdown':0x1008ff03, 'xf86kbdlightonoff':0x1008ff04, 'xf86kbdbrightnessup':0x1008ff05,
                    'xf86kbdbrightnessdown':0x1008ff06, 'xf86standby':0x1008ff10, 'xf86audiolowervolume':0x1008ff11, 'xf86audiomute':0x1008ff12, 'xf86audioraisevolume':0x1008ff13,
                    'xf86audioplay':0x1008ff14, 'xf86audiostop':0x1008ff15, 'xf86audioprev':0x1008ff16, 'xf86audionext':0x1008ff17, 'xf86homepage':0x1008ff18,
                    'xf86mail':0x1008ff19, 'xf86start':0x1008ff1a, 'xf86search':0x1008ff1b, 'xf86audiorecord':0x1008ff1c, 'xf86calculator':0x1008ff1d,
                    'xf86memo':0x1008ff1e, 'xf86todolist':0x1008ff1f, 'xf86calendar':0x1008ff20, 'xf86powerdown':0x1008ff21, 'xf86contrastadjust':0x1008ff22,
                    'xf86rockerup':0x1008ff23, 'xf86rockerdown':0x1008ff24, 'xf86rockerenter':0x1008ff25, 'xf86back':0x1008ff26, 'xf86forward':0x1008ff27,
                    'xf86stop':0x1008ff28, 'xf86refresh':0x1008ff29, 'xf86poweroff':0x1008ff2a, 'xf86wakeup':0x1008ff2b, 'xf86eject':0x1008ff2c,
                    'xf86screensaver':0x1008ff2d, 'xf86www':0x1008ff2e, 'xf86sleep':0x1008ff2f, 'xf86favorites':0x1008ff30, 'xf86audiopause':0x1008ff31,
                    'xf86audiomedia':0x1008ff32, 'xf86mycomputer':0x1008ff33, 'xf86vendorhome':0x1008ff34, 'xf86lightbulb':0x1008ff35, 'xf86shop':0x1008ff36,
                    'xf86history':0x1008ff37, 'xf86openurl':0x1008ff38, 'xf86addfavorite':0x1008ff39, 'xf86hotlinks':0x1008ff3a, 'xf86brightnessadjust':0x1008ff3b,
                    'xf86finance':0x1008ff3c, 'xf86community':0x1008ff3d, 'xf86audiorewind':0x1008ff3e, 'xf86backforward':0x1008ff3f, 'xf86launch0':0x1008ff40,
                    'xf86launch1':0x1008ff41, 'xf86launch2':0x1008ff42, 'xf86launch3':0x1008ff43, 'xf86launch4':0x1008ff44, 'xf86launch5':0x1008ff45,
                    'xf86launch6':0x1008ff46, 'xf86launch7':0x1008ff47, 'xf86launch8':0x1008ff48, 'xf86launch9':0x1008ff49, 'xf86launcha':0x1008ff4a,
                    'xf86launchb':0x1008ff4b, 'xf86launchc':0x1008ff4c, 'xf86launchd':0x1008ff4d, 'xf86launche':0x1008ff4e, 'xf86launchf':0x1008ff4f,
                    'xf86applicationleft':0x1008ff50, 'xf86applicationright':0x1008ff51, 'xf86book':0x1008ff52, 'xf86cd':0x1008ff53, 'xf86calculater':0x1008ff54,
                    'xf86clear':0x1008ff55, 'xf86close':0x1008ff56, 'xf86copy':0x1008ff57, 'xf86cut':0x1008ff58, 'xf86display':0x1008ff59,
                    'xf86dos':0x1008ff5a, 'xf86documents':0x1008ff5b, 'xf86excel':0x1008ff5c, 'xf86explorer':0x1008ff5d, 'xf86game':0x1008ff5e,
                    'xf86go':0x1008ff5f, 'xf86itouch':0x1008ff60, 'xf86logoff':0x1008ff61, 'xf86market':0x1008ff62, 'xf86meeting':0x1008ff63,
                    'xf86menukb':0x1008ff65, 'xf86menupb':0x1008ff66, 'xf86mysites':0x1008ff67, 'xf86new':0x1008ff68, 'xf86news':0x1008ff69,
                    'xf86officehome':0x1008ff6a, 'xf86open':0x1008ff6b, 'xf86option':0x1008ff6c, 'xf86paste':0x1008ff6d, 'xf86phone':0x1008ff6e,
                    'xf86q':0x1008ff70, 'xf86reply':0x1008ff72, 'xf86reload':0x1008ff73, 'xf86rotatewindows':0x1008ff74, 'xf86rotationpb':0x1008ff75,
                    'xf86rotationkb':0x1008ff76, 'xf86save':0x1008ff77, 'xf86scrollup':0x1008ff78, 'xf86scrolldown':0x1008ff79, 'xf86scrollclick':0x1008ff7a,
                    'xf86send':0x1008ff7b, 'xf86spell':0x1008ff7c, 'xf86splitscreen':0x1008ff7d, 'xf86support':0x1008ff7e, 'xf86taskpane':0x1008ff7f,
                    'xf86terminal':0x1008ff80, 'xf86tools':0x1008ff81, 'xf86travel':0x1008ff82, 'xf86userpb':0x1008ff84, 'xf86user1kb':0x1008ff85,
                    'xf86user2kb':0x1008ff86, 'xf86video':0x1008ff87, 'xf86wheelbutton':0x1008ff88, 'xf86word':0x1008ff89, 'xf86xfer':0x1008ff8a,
                    'xf86zoomin':0x1008ff8b, 'xf86zoomout':0x1008ff8c, 'xf86away':0x1008ff8d, 'xf86messenger':0x1008ff8e, 'xf86webcam':0x1008ff8f,
                    'xf86mailforward':0x1008ff90, 'xf86pictures':0x1008ff91, 'xf86music':0x1008ff92, 'xf86battery':0x1008ff93, 'xf86bluetooth':0x1008ff94,
                    'xf86wlan':0x1008ff95, 'xf86uwb':0x1008ff96, 'xf86audioforward':0x1008ff97, 'xf86audiorepeat':0x1008ff98, 'xf86audiorandomplay':0x1008ff99,
                    'xf86subtitle':0x1008ff9a, 'xf86audiocycletrack':0x1008ff9b, 'xf86cycleangle':0x1008ff9c, 'xf86frameback':0x1008ff9d, 'xf86frameforward':0x1008ff9e,
                    'xf86time':0x1008ff9f, 'xf86select':0x1008ffa0, 'xf86view':0x1008ffa1, 'xf86topmenu':0x1008ffa2, 'xf86red':0x1008ffa3,
                    'xf86green':0x1008ffa4, 'xf86yellow':0x1008ffa5, 'xf86blue':0x1008ffa6, 'xf86_switch_vt_1':0x1008fe01, 'xf86_switch_vt_2':0x1008fe02,
                    'xf86_switch_vt_3':0x1008fe03, 'xf86_switch_vt_4':0x1008fe04, 'xf86_switch_vt_5':0x1008fe05, 'xf86_switch_vt_6':0x1008fe06, 'xf86_switch_vt_7':0x1008fe07,
                    'xf86_switch_vt_8':0x1008fe08, 'xf86_switch_vt_9':0x1008fe09, 'xf86_switch_vt_10':0x1008fe0a, 'xf86_switch_vt_11':0x1008fe0b, 'xf86_switch_vt_12':0x1008fe0c,
                    'xf86_ungrab':0x1008fe20, 'xf86_cleargrab':0x1008fe21, 'xf86_next_vmode':0x1008fe22, 'xf86_prev_vmode':0x1008fe23 }
        self.toggled_keys = []

    def get_key_code(self, key):
        if type(key) == type(""):
            if self.keys.has_key(key.lower()):
                return self.keys[key.lower()]
            else:
                if len(key) > 0:
                    return 0
                else:
                    return ord(key)
        else:
            return key

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
            self.key_emulator.press_keysym(key_codes)

    def release_key(self, key_codes):
        key_codes = self.convert_key(key_codes)
        if type(key_codes) == type([]):
            for key_code in reversed(key_codes):
                self.key_emulator.release_keysym(key_code)
        else:
            self.key_emulator.release_keysym(key_codes)

    def toggle_key(self, key_codes):
        key_codes = self.get_key_code(key_codes)
        if key_codes in self.toggled_keys:
            self.release_key(key_codes)
            self.toggled_keys.remove(key_codes)
        else:
            self.hold_key(key_codes)
            self.toggled_keys.append(key_codes)

    def press_key(self, key_codes):
        self.hold_key(key_codes)
        self.release_key(key_codes)
