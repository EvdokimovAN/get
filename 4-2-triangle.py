import RPi.GPIO as GPIO
import time

    
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    period = float(input())
    while True:
        for i in range(256):
            time.sleep(period/512)
            for k in range(8):
                GPIO.output(dac[k], dec2bin(i)[k])
        for i in range(254,0,-1):
            time.sleep(period/512)
            for k in range(8):
                GPIO.output(dac[k], dec2bin(i)[k])



finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    
    