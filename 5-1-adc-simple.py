import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def decimal_to_binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        dec_i=decimal_to_binary(i)
        GPIO.output(dac,dec_i)
        time.sleep(0.001)
        compValue =GPIO.input(comp)
        if compValue ==1:
            return i
try:
    while True:
        digital_value = adc()
        if digital_value == None:
            digital_value = 256

        
        voltage = int(digital_value)/256*3.3
        print(digital_value, voltage)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
