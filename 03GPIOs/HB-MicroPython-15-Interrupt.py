from machine import Pin
from time import sleep

btn = Pin(4, Pin.IN)
led = Pin(5, Pin.OUT)

def my_fun(pin):
    if (btn.value()):
        led.value(1)
    else:
        led.value(0)
        
btn.irq(my_fun)
