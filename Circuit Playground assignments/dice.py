from adafruit_circuitplayground import cp
import random
import time

while True:
     if cp.button_a:
          for i in range(0,(random.randint(0,10))):
               cp.pixels[i] = (0,0,255)
               while cp.button_a:
                    pass
     if cp.button_b:
          cp.pixels.fill((0,0,0))