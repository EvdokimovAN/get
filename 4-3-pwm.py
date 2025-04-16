import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
pwm = GPIO.PWM(24,1000)
pwm.start(0)
try:
    while True:
        duty = float(input())

        pwm.ChangeDutyCycle(duty)
        v = 3.3 * duty/100
        print(v,' ожидаемое напряжение')
        
finally:
    pwm.stop()
    GPIO.cleanup()
