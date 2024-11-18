from adafruit_circuitplayground import cp
import time
while True:
    
   
    cp.pixels.fill((0, 0, 255))
    cp.play_tone(500, 1)
    cp.pixels.fill((255, 0, 0))
    cp.play_tone(900,1)