import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
lan = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(lan,GPIO.OUT)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    answer = 0
    an = binary(128)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=128   

    an = binary(64+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=64


    an = binary(32+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=32


    an = binary(16+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=16


    an = binary(8+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=8


    an = binary(4+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=4


    an = binary(2+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=2


    an = binary(1+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 0:
        answer +=1


    return answer
    
try:
    while True:
        digital_value = adc()
        GPIO.output(lan,binary(digital_value))
        if digital_value == None:
            digital_value = 256


        
        voltage = int(digital_value)/256*3.3
        print(digital_value, voltage)

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()
