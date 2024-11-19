from adafruit_circuitplayground import cp
import time
import random 

cp.pixels.brightness = 0.3  # Set brightness to 30%


while True:
    if cp.light >=30:
        cp.pixels[0]=((0, 0, 255))
    
    elif cp.light >= 27:
        cp.pixels[0]=(0,0,255)
    elif cp.light >= 27:
        cp.pixels[1]=(0,0,255)
    elif cp.light >= 24:
        cp.pixels[2]=(0,0,255)
    elif cp.light >= 21:
        cp.pixels[3]=(0,0,255)
    elif cp.light >= 18:
        cp.pixels[4]=(0,0,255)
    elif cp.light >= 15:
        cp.pixels[5]=(0,0,255)
    elif cp.light >= 12:
        cp.pixels[6]=(0,0,255)
    elif cp.light >= 9:
        cp.pixels[7]=(0,0,255)
    elif cp.light >= 6:
        cp.pixels[8]=(0,0,255)
    elif cp.light >= 3:
        cp.pixels[9]=(0,0,255)
