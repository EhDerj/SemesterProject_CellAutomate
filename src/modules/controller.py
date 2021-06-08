import os
import datetime
import Model
import View
import time
import objects

class Controller:


    def __init__(self):
        self._delay = 0.1

    def __main__(self):
        while True:
            self.iterate()

    def iterate(self):
        past = datetime.datetime.now().time()
        self.drawColors(objects.LifeMap.lifeMap)
        present = datetime.datetime.now().time()
        self.pause(past, present, self._delay)

    def setDelay(self, delay):
        _delay = delay

    def drawColors(self, lifeMap):
        arr = objects.LifeMap.lifeMap.getCellMatrix()
        for i in range(len(arr)):
            for j in range(len(len(arr))):
                objects.ColorMap.colorMap[i][j] = objects.Colors.swapColor(arr[i][j])
        return objects.ColorMap.colorMap
        
    def pause(self, past, present, delay):
        res = delay - (present - past)
        time.sleep(res)