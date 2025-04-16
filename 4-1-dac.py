import RPi.GPIO as GPIO
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def bi(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    a=0
    while True:
        try:
            a = input('Введите число от 0 до 255  ')
            if a =='q':
                break
            k = float(a)
            
            
            if k%1!=0:
                print('ввод не целого числа')
                continue
            if k<0:
                print('ввод отрицательного значения')
                continue
            if k>255:
                print('ввод значения превышающего возможности 8-разрядного ЦАП')
                continue
            b = int(a)

        
            for i in range(8):
                GPIO.output(dac[i], bi(b)[i])
            
            V = 3.3 * (b/255)
            print(f'Предполагаемое напряжение {V:.2f}')

        except ValueError:
            print('ввода не числового значения')
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    
    
