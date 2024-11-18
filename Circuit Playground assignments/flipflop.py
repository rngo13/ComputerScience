
from adafruit_circuitplayground import cp

import time

while True:
    if cp.switch:
        cp.pixels[0] = (255, 0, 0)   # Pixel 0 turns red
        cp.pixels[1] = (0, 255, 0)   # Pixel 1 turns green
        cp.pixels[2] = (0, 0, 255)   # Pixel 2 turns blue
        cp.pixels[3] = (0, 0, 255)   # Pixel 2 turns blue
        cp.pixels[4] = (0, 0, 255)   # Pixel 2 turns blue
        cp.pixels[5] = (0, 0, 0)   # Pixel 0 turns red
        cp.pixels[6] = (0, 0, 0)   # Pixel 1 turns green
        cp.pixels[7] = (0, 0, 0)   # Pixel 2 turns blue
        cp.pixels[8] = (0, 0, 0)   # Pixel 2 turns blue
        cp.pixels[9] = (0, 0, 0)   # Pixel 2 turns blue
    else:
        cp.pixels[0] = (0, 0, 0)   # Pixel 0 turns red
        cp.pixels[1] = (0, 0, 0)   # Pixel 1 turns green
        cp.pixels[2] = (0, 0, 0)   # Pixel 2 turns blue
        cp.pixels[3] = (0, 0, 0)   # Pixel 2 turns blue
        cp.pixels[4] = (0, 0, 0)   # Pixel 2 turns blue
        cp.pixels[5] = (255, 0, 0)   # Pixel 0 turns red
        cp.pixels[6] = (0, 255, 0)   # Pixel 1 turns green
        cp.pixels[7] = (0, 0, 255)   # Pixel 2 turns blue
        cp.pixels[8] = (0, 0, 255)   # Pixel 2 turns blue
        cp.pixels[9] = (0, 0, 255)   # Pixel 2 turns blue



   

