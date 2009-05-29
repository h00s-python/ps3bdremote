#!/usr/bin/python

import ps3bdremote
import os
from time import sleep
from virtualkey import VirtualKey

if __name__ == '__main__':
    remote = ps3bdremote.PS3BDRemote("00:21:4F:A6:14:B6") # replace with your PS3 remote id
    keys = VirtualKey()

    while True:
        if remote.connect():
            print "Connected"
            break
        sleep(1)
        print "Trying to connect to PS3 BD Remote..."

    while True:
        command = remote.get_command()
        if command == "play":
            keys.press_key("xf86audioplay")
        elif command == "next":
            keys.press_key("xf86audionext")
        elif command == "prev":
            keys.press_key("xf86audioprev")
        elif command == "r1":
            keys.press_key("xf86audioraisevolume")
        elif command == "r3":
            keys.press_key("xf86audiolowervolume")
        elif command == "circle":
            keys.press_key(["alt_left", "f4"])
        elif command == "eject":
            keys.press_key("esc")
        elif command == "enter":
            keys.press_key("enter")
        elif command == "display":
            # start tvtime
            os.system("nohup tvtime 2> /dev/null &")
        elif command == "square":
            keys.toggle_key("alt_left")
        elif command == "triangle":
            keys.press_key("tab")
        elif command == "up":
            keys.press_key("arrow_up")
        elif command == "down":
            keys.press_key("arrow_down")
        elif command == "left":
            keys.press_key("arrow_left")
        elif command == "right":
            keys.press_key("arrow_right")

