# PS3 BD Remote class - ver. 0.1
# Depends on python-bluez
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

import bluetooth

class PS3BDRemote(object):

    def __init__(self, address):
        self.device_address = address
        self.keys = { 'a10100000016':'eject', 'a10100000000':'1', 'a10100000001':'2', 'a10100000002':'3',
                      'a10100000064':'audio', 'a10100000003':'4', 'a10100000004':'5', 'a10100000005':'6',
                      'a10100000065':'angle', 'a10100000006':'7', 'a10100000007':'8', 'a10100000008':'9',
                      'a10100000063':'subtitle', 'a1010000000f':'clear', 'a10100000009':'0', 'a10100000028':'time',
                      'a10100000081':'red', 'a10100000082':'green', 'a10100000083':'yellow', 'a10100000080':'blue',
                      'a10100000070':'display', 'a1010000001a':'topmenu', 'a10100000040':'popupmenu', 'a1010000000e':'return',
                      'a1010010005c':'triangle', 'a10110000054':'up', 'a1010020005d':'circle',
                      'a10180000057':'left', 'a1010000080b':'enter', 'a10120000055':'right',
                      'a1010080005f':'square', 'a10140000056':'down', 'a1010040005e':'x',
                      'a1010004005a':'l1', 'a10100000143':'psbutton', 'a1010008005b':'r1',
                      'a10100010058':'l2', 'a10100020059':'r2',
                      'a10102000051':'l3', 'a10101000050':'select', 'a10104000052':'r3',
                      'a10100000033':'rewind', 'a10100000032':'play', 'a10100000034':'forward',
                      'a10100000030':'prev', 'a10100000038':'stop', 'a10100000031':'next',
                      'a10100000060':'slowrewind', 'a10100000039':'pause', 'a10100000061':'slowforward',
                      'a101003000ff':'triangle+circle', 'a101009000ff':'triangle+square', 'a101005000ff':'triangle+x',
                      'a10100a000ff':'circle+square', 'a101006000ff':'circle+x', 'a10100c000ff':'square+x',
                      'a101900000ff':'left+up', 'a101600000ff':'left+down', 'a101300000ff':'right+up', 'a101600000ff':'right+down',
                      'a101000000ff':'releasedbutton' }

    def connect(self):
        try:
            self.blue = bluetooth.BluetoothSocket(bluetooth.L2CAP)
            self.blue.connect((self.device_address, 19))
            return True
        except:
            return False
    
    def get_command(self):
        received_data = self.blue.recv(1024)
        received_data = received_data.encode('hex')[0:12]
        if self.keys.has_key(received_data):
            return self.keys[received_data]
        else:
            return 'unknown'

    def disconnect(self):
        try:
            self.blue.disconnect()
            return True
        except:
            return False
