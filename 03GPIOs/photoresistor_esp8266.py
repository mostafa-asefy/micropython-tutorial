from machine import Pin, ADC
from time import sleep

pr = ADC(0)
led = Pin(12, Pin.OUT)

while(True):
    print(pr.read())
    print("led", led.value())
    
    if (pr.read() < 800):
        led.value(1)
    else:
        led.value(0)
        
    sleep(0.3)