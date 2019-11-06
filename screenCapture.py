# -*- coding: utf-8 -*-
#mindig mindenhez
import numpy as np
#a képernyő figyeléséhez
from PIL import ImageGrab
#képfeldolgozáshoz
import cv2
#fps ellenőrzés
import time


#fpshez az első timestamp
lastTick = time.time()
#végtelen ciklus - q-t lenyomva lép ki
while(True):
    #képernyőkép megszerzése PIL-lel
    printscreen_pil =  ImageGrab.grab()
    #képernyőkép átalakítása numpy array-ra (RGB)
    screen = np.array(printscreen_pil)  
    #szürkeárnyalatossá alakítás
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
    #kép elmosása az éldetekcióhoz
    blur = cv2.GaussianBlur(screen, (15,15), cv2.BORDER_DEFAULT)
    #éldetekció Canny algoritmussal
    edges = cv2.Canny(blur, 60,80)
    
    #fps számítása
    fps = 1/(time.time()-lastTick)
    print('FPS: %f ' % fps)
    #timestamp következő fpshez
    lastTick = time.time()
    
    #kép megjelenítése
    cv2.imshow('edges', edges)
    
    #q-ra lépj ki
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break