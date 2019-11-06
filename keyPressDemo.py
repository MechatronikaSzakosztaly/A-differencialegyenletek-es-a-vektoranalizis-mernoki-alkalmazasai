# -*- coding: utf-8 -*-

#időzítéshez
import time

#billentyű események emulálásához
from pressKeys import PressKey, ReleaseKey, W,A,S,D

#érdemes az elején késleltetni egy kicsit, hogy legyen időnk megnyitne a játékot
time.sleep(4)

#nyomd 2 mp-ig a W-t (menj előre)
PressKey(W)
time.sleep(2)

#engedd el a W-t és fékezz 2 mp-ig
ReleaseKey(W)
PressKey(S)
time.sleep(2)
ReleaseKey(S)