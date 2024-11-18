# we first need to inport board specific tools
# every project for this board will need this statement
from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.1
while True:
  
    cp.pixels.fill((0, 0, 0))   # Pixel 0 turns red
    time.sleep(.367)
    cp.pixels.fill((0, 255, 0))   # Pixel 1 turns green
    time.sleep(.367)
    cp.pixels.fill((0, 0, 0))   # Pixel 2 turns blue


   

