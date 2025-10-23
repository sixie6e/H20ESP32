from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import time, sys

i2c = I2C(0, sda=Pin(21, pull=Pin.PULL_UP), scl=Pin(22, pull=Pin.PULL_UP))
screen = SSD1306_I2C(128, 64, i2c)
screen.fill(0)
screen.rect(0, 0, 127, 63, 1)
screen.text("   WATER PUMP:", 5, 2, 1)
screen.text("   en/disabled", 5, 12, 1)
screen.text("    AIR PUMP:", 5, 22, 1)
screen.text("   en/disabled", 5, 32, 1)
screen.text("   STATE READY", 5, 42, 1)
screen.show()
pwm_ena = PWM(Pin(ena), freq=100, duty=0)
pwm_enb = PWM(Pin(enb), freq=100, duty=0)
water_pump_in1 = machine.Pin(18, machine.Pin.OUT)
water_pump_in2 = machine.Pin(19, machine.Pin.OUT)
air_pump_in1 = machine.Pin(22, machine.Pin.OUT)
air_pump_in2 = machine.Pin(23, machine.Pin.OUT)

def set_water_pump(state):
    if state:
        water_pump_in1.value(1) # on
        water_pump_in2.value(0)
    else:
        water_pump_in1.value(0) # off
        water_pump_in2.value(0)

def set_air_pump(state):
    if state:
        air_pump_in1.value(1)
        air_pump_in2.value(0)
    else:
        air_pump_in1.value(0) 
        air_pump_in2.value(0)

while True:
    try:
        command = sys.stdin.readline().strip()
        if command == 'water_pump_on':
            set_water_pump(True)
        elif command == 'water_pump_off':
            set_water_pump(False)
        elif command == 'air_pump_on':
            set_air_pump(True)
        elif command == 'air_pump_off':
            set_air_pump(False)
    except Exception as e:
        print("Error:", e)
