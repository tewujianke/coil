"""
Guanduo Li
A python script to enhance PUBG
"""

from __future__ import print_function

import win32api
import win32con
import time
import os
import sys
from enum import Enum
import threading

class guns(Enum):
    EMPTY = 0
    SCAR = 1
    M16 = 2
    M416 = 3
    AKA = 4
    UZI = 5
    UMP = 6

class Gun(object):

    def __init__(self,gun_id,recoil_seq,rounds_per_min):
        scalar = 0.2
        self.gun_id = gun_id
        self.recoil_seq = [int(x*scalar) for x in recoil_seq]
        self.rounds_per_min = rounds_per_min

        self.time_between_shots = time_between_shots

    def get_recoil(self):
        return self.recoil_seq

class Uzi(Gun):

    def __init__(self):
        recoil = [137,75,75,75,75,75,75,75,75,75,75,75,75]
        fire_spd = 600
        Gun.__init__(self,guns.UZI,recoil,fire_spd)
    
class aid(object):

    def __init__(self):
        self.current_gun = guns.EMPTY

"""
Multithreading for user's keyboard control
"""        
class menu_thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.activate = 0
        
    def run(self):
        while 1:
            a = win32api.GetAsyncKeyState(win32con.VK_NUMPAD7)
            if a:
                #a = win32api.GetAsyncKeyState(win32con.VK_NUMPAD7)
                while a:
                    a = win32api.GetAsyncKeyState(win32con.VK_NUMPAD7)
                self.activate = ~self.activate
                print("activate=%d"%self.activate)
                if self.activate:
                    print("\a")
            
            
    def is_activate(self):
        if self.activate:
            return True
        else:
            return False

        
if __name__ == '__main__':
    activate = 0

    t = menu_thread()
    t.start()
    
    a = Uzi()
    print(a.get_recoil())
    current_gun = Uzi()
    count = 0
    while 1:
        a = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
        while a != 0 and t.is_activate():
            time.sleep(current_gun.time_between_shots)
            (curx,cury) = win32api.GetCursorPos()
            y = cury+current_gun.get_recoil()[count]
            win32api.SetCursorPos((curx,y))
            count+=1
            if count == len(current_gun.get_recoil()):
                count = 0
            a = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
            if not a:
                count = 0
            time.sleep(1.0/((1000.0*2+2))/60)
        


        
