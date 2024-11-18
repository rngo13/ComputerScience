from adafruit_circuitplayground import cp
import time

x=0
while True:

    if cp.button_a:
        cp.pixels.fill((0,0,0))
        x=x+1
        for i in range(x):
            cp.pixels[i]=(0,255,0)
    time.sleep(.30)

    if cp.button_b:
        cp.pixels.fill((0,0,0))
        x=x - 1
        for i in range(x):
            cp.pixels[i]=(0,255,0)
    time.sleep(.30)

