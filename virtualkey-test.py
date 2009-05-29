from time import sleep
from virtualkey import VirtualKey
import thread

keys = VirtualKey()

# write abc
def example1():
    sleep(1)
    keys.press_key("a")
    keys.press_key("b")
    keys.press_key("c")
    keys.press_key("enter")

# switch opened windows with alt tab - 3x alt tab
def example2():
    sleep(1)
    keys.toggle_key("alt_left")
    keys.press_key("tab")
    sleep(1)
    keys.press_key("tab")
    sleep(1)
    keys.press_key("tab")
    sleep(1)
    keys.toggle_key("alt_left")

# break script with ctrl-c
def example3():
    sleep(1)
    keys.press_key(["ctrl_left", "c"])

#####!!! uncomment one of the next lines to test examples !!!####
thread.start_new_thread(example1, ())
#thread.start_new_thread(example2, ())
#thread.start_new_thread(example3, ())

raw_input('wait for input: ')
