from machine import Pin, PWM, I2C
from ssd1306 import SSD1306_I2C
import time

ena = 32
in1 = 33
in2 = 34
pwm_ena = PWM(Pin(ena), freq=100, duty=0)
in1 = Pin(in1, Pin.OUT)
in2 = Pin(in2, Pin.OUT)
in1.value(0)
in2.value(0)
enb = 21
in3 = 19
in4 = 18
pwm_enb = PWM(Pin(enb), freq=100, duty=0)
in3 = Pin(in3, Pin.OUT)
in4 = Pin(in4, Pin.OUT)
in3.value(0)
in4.value(0)
i2c = I2C(0, sda=Pin(19, pull=Pin.PULL_UP, scl=Pin(18, pull=Pin.PULL_UP))
oled = SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.rect(0, 0, 127, 63, 1)

# water
def w_motor_speed(wspeed):
    # (0-1023) for a 10-bit PWM duty cycle.
        if 0 <= wspeed <= 1023:
        pwm_ena.duty(wspeed)
        oled.text(wspeed, 5, 12, 1)
    else:
        print("Speed must be between 0 and 1023")

def w_run_pump(direction, wspeed):
    if direction == 1: 
        in1.value(1)
        in2.value(0)
        set_wmotor_speed(wspeed)
        print(f"Pump engaged @ {wspeed}")
    else:
        in1.value(0)
        in2.value(0)
        set_wmotor_speed(0)
        print("Pump disengaged.")

try:
    print("Pump engaging...")
    # example usage:
    w_run_pump(1, 512)
    time.sleep(5)
    w_run_pump(1, 1023)
    time.sleep(3)
    w_run_pump(0, 0)
    time.sleep(2)
    print("Sequence complete. Pump disengaged.")
except KeyboardInterrupt:
    print("User interrupt. Pump disengaging.")
    w_run_pump(0, 0)
except Exception as e:
    print(f"Error: {e}")
    w_run_pump(0, 0)

# air
def a_motor_speed(aspeed):
    # (0-1023) for a 10-bit PWM duty cycle.
        if 0 <= speed <= 1023:
        pwm_enb.duty(aspeed)
        oled.text(aspeed, 5, 22, 1)
    else:
        print("Speed must be between 0 and 1023")

def a_run_pump(direction, aspeed):
    if direction == 1: 
        in3.value(1)
        in4.value(0)
        set_amotor_speed(aspeed)
        print(f"Pump engaged @ {aspeed}")
    else:
        in3.value(0)
        in4.value(0)
        set_amotor_speed(0)
        print("Pump disengaged.")

try:
    print("Pump engaging...")
    # example usage:
    a_run_pump(1, 512)
    time.sleep(5)
    a_run_pump(1, 1023)
    time.sleep(3)
    a_run_pump(0, 0)
    time.sleep(2)
    print("Sequence complete. Pump disengaged.")
except KeyboardInterrupt:
    print("User interrupt. Pump disengaging.")
    a_run_pump(0, 0)
except Exception as e:
    print(f"Error: {e}")
    a_run_pump(0, 0)
