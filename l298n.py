from machine import Pin, PWM
import time

ena = 23
in1 = 19
in2 = 18
pwm_ena = PWM(Pin(ena), freq=100, duty=0)
in1 = Pin(in1, Pin.OUT)
in2 = Pin(in2, Pin.OUT)
in1.value(0)
in2.value(0)

def set_motor_speed(speed):
        if 0 <= speed <= 1023:
        pwm_ena.duty(speed)
    else:
        print("Error.")

def run_pump(direction, speed):
    if direction == 1: 
        in1.value(1)
        in2.value(0)
        set_motor_speed(speed)
        print(f"Pump engaged @ {speed}")
    else:
        in1.value(0)
        in2.value(0)
        set_motor_speed(0)
        print("Pump disengaged.")

try:
    print("Pump engaging...")
    # example usage:
    run_pump(1, 512)
    time.sleep(5)
    run_pump(1, 1023)
    time.sleep(3)
    run_pump(0, 0)
    time.sleep(2)
    print("Sequence complete. Pump disengaged.")
except KeyboardInterrupt:
    print("User interrupt. Pump disengaging.")
    run_pump(0, 0)
except Exception as e:
    print(f"Error: {e}")
    run_pump(0, 0)
