'''

LDR (Light Dependent Resistor)
- alat yang digunakan untuk mendeteksi cahaya

'''

import RPi.GPIO as GPIO #Modul python untuk mengendalikan GPIO (general purpose input and output) pada Raspberry Pi.

sensorPin = 7
ledPin = 8

# menyetel mode pin numbering pada Raspberry Pi board menjadi mode BOARD.
GPIO.setmode(GPIO.BOARD)
# mengatur channel menjadi mode input/reading agar dapat membaca hasil inputan dari sensor
GPIO.setup(sensorPin, GPIO.IN)
# mengatur channel menjadi mode output/writing agar dapat mengatur nilainya
GPIO.setup(ledPin, GPIO.OUT) 

try:
    while True:
        if GPIO.input(sensorPin) == GPIO.HIGH:
            GPIO.output(ledPin, GPIO.HIGH) # mengatur nilai channel menjadi High/1/True.
            print('lampu menyala')    
        else:
            GPIO.output(ledPin, GPIO.LOW) # mengatur nilai channel menjadi Low/0/False.
            print('lampu padam')  
except:
    GPIO.cleanup()