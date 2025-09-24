import machine
import sys

peltier1 = machine.Pin(8, machine.Pin.OUT)
peltier2 = machine.Pin(9, machine.Pin.OUT)
peltier3 = machine.Pin(10, machine.Pin.OUT)
peltier4 = machine.Pin(11, machine.Pin.OUT)
peltier5 = machine.Pin(12, machine.Pin.OUT)

def set_peltier1(state):
	peltier1.value(1) if state else peltier1.value(0)
def set_peltier2(state):
	peltier2.value(1) if state else peltier2.value(0)
def set_peltier3(state):
	peltier3.value(1) if state else peltier3.value(0)
def set_peltier4(state):
	peltier4.value(1) if state else peltier4.value(0)
def set_peltier5(state):
	peltier5.value(1) if state else peltier5.value(0)

while True:
	try:
		command = sys.stdin.readline().strip()
		if command == 'peltier1_on':
			set_peltier1(True)
		elif command == 'peltier2_on':
			set_peltier2(True)
		elif command == 'peltier2_off':
			set_peltier2(False)
		elif command == 'peltier3_on':
			set_peltier3(True)
		elif command == 'peltier3_off':
			set_peltier3(False)
		elif command == 'peltier4_on':
			set_peltier4(True)
		elif command == 'peltier4_off':
			set_peltier4(False)
		elif command == 'peltier5_on':
			set_peltier5(True)
		elif command == 'peltier5_off':
			set_peltier5(False)
	except Exception as e:
		print("Error:", e)
