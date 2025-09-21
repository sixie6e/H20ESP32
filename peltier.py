from machine import ADC, Pin
import time
adc_pin= 22
peltier_pin = 17
target_temp = 20
hysteresis = 1
beta = 3950
ref_r = 10000
ref_t = 20 + 273.15
nom_r = 10000
adc = ADC(Pin(adc_pin))
adc.width(ADC.WIDTH_12BIT)
adc.attn(ADC.ATTN_11DB)
peltier = Pin(peltier_pin, Pin.OUT)

def read_temp():
    adc_value = adc.read()
    voltage = (adc_value/4095.0)*3.3    
    if voltage == 0:
        return None
    resistance = (3.3*ref_r/voltage)-ref_r    
    try:
        # I had help with this and I still don't understand why it works.
        b_function = 1/((1/ref_t)+(1/beta)*(resistance/nom_r))
        # b_function = 1/((1/290.15)+(1/3950)*(resistance/10000))
        return b_function-273.15
    except ZeroDivisionError:
        return None

def peltier_control(temp):
    if temp is None:
        peltier.value(0)
        print("Invalid temp reading.")
        return
    if temp > target_temp + hysteresis:
        peltier.value(1)
        print(f"{temp:.2f} C is above threshold. System engaged.")
    elif temp < target_temp:
        peltier.value(0)
        print(f"{temp:.2f} C is within bounds. System disengaged.")
    else:
        print("Temp is stable.")
        
while True:
    try:
        current_temp = read_temp()
        peltier_control(current_temp)
    except Exception as e:
        print(f"Problem: {e}")
