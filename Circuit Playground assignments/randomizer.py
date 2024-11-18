from adafruit_circuitplayground import cp
import random
import time

while True:
     x, y, z = cp.acceleration
     shake_threshold = 15.0
     if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
          for i in range(0,10):
               cp.pixels[i]= (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))