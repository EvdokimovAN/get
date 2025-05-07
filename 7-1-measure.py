import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setwarnings(False)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
# , initial=GPIO.HIGH)
start = time.time()
znach = []
GPIO.output(troyka, GPIO.LOW)
def binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    answer = 0
    an = binary(128)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=128   

    an = binary(64+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=64


    an = binary(32+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=32


    an = binary(16+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=16


    an = binary(8+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=8


    an = binary(4+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=4


    an = binary(2+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=2


    an = binary(1+answer)
    GPIO.output(dac,an)
    time.sleep(0.001)
    if GPIO.input(comp) == 1:
        answer +=1


    return answer

try:
    while True:
        voltage = adc()
        #print(f"Полученное значение напряжения вперед: {voltage:.4f}")
        znach.append(voltage*3.3/256)
        if voltage >= 245:
           break
    
    GPIO.output(troyka, GPIO.HIGH)
    while True:
        voltage = adc()
        #print(f"Полученное значение напряжения назад: {voltage:.4f}")
        znach.append(voltage*3.3/256)
        if voltage <= 80:
            break
finally:
    end = time.time()
    prod = end - start

    print(f"Общая продолжительность эксперимента: {prod:.2f} секунд")

    if len(znach) > 1:
        period = prod / len(znach)
        rate = 1 / period
        st = (3.3 / (2 ** 8))

        print(f"Период одного измерения: {period:.4f} секунд")
        print(f"Частота: {rate:.2f} Гц")
        print(f"Шаг квантования АЦП: {st:.4f} В")

        with open('data.txt', 'w') as data_file:
            for voltage in znach:
                data_file.write(f"{voltage:.4f}\n")

        with open('settings.txt', 'w') as settings_file:
            settings_file.write(f"Частота: {rate:.2f} Гц\n")
            settings_file.write(f"Шаг квантования АЦП: {st:.4f} В\n")
        vrem = []
        for i in range(len(znach)):
            vrem.append(period*i)


        plt.plot(vrem, znach)
        plt.xlabel('Время, с')
        plt.ylabel('Напряжение (В)')
        plt.title('Зависимость показаний АЦП от номера измерения')
        plt.show()

    GPIO.cleanup()
