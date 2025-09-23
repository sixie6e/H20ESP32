import machine
import sys

PELTIER1_PIN = machine.Pin(8, machine.Pin.OUT)
PELTIER2_PIN = machine.Pin(9, machine.Pin.OUT)

def set_peltier1(state):
	PELTIER1_PIN.value(1) if state else PELTIER1_PIN.value(0)
    
def set_peltier2(state):
	PELTIER2_PIN.value(1) if state else PELTIER2_PIN.value(0)

while True:
	try:
		command = sys.stdin.readline().strip()
		if command == 'PELTIER1_ON':
			set_peltier1(True)
		elif command == 'PELTIER2_ON':
			set_peltier2(True)
		elif command == 'PELTIER2_OFF':
			set_peltier2(False)
	except Exception as e:
		print("Error:", e)
