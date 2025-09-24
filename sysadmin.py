import serial
import time

r3port = 'COM3'
wroom32port = 'COM4'
c3port = 'COM5'
baud = 9600
water_threshold = 500
temperature_threshold_high = -90.0 
temperature_threshold_low = -110.0 

try:
	r3_serial = serial.Serial(r3port, baud, timeout=1)
	wroom32_serial = serial.Serial(wroom32port, baud, timeout=1)
	c3_serial = serial.Serial(c3port, baud, timeout=1)
	time.sleep(2)
except serial.SerialException as e:
	print(f"Error opening serial port: {e}")
	exit()

def send_command(ser_port_command):
	try:
		ser_port.write(f"{command}\n".encode())
		print(f"Sent to {ser_port.name}: {command}")
	except serial.SerialException as e:
		print(f"Error sending command to {ser_port.name}: {e}")

def main():
    print("Starting system administration...")
    while True:
        try:
            line = ser_r3.readline().decode('utf-8').strip()
            if line:
                print(f"Received from R3: {line}")                
                parts = line.split(',')
                temp_str = parts[0].split(':')[1]
                water_str = parts[1].split(':')[1]
                temperature = float(temp_str)
                water_level = int(water_str)                
                print(f"Temperature: {temperature}°C, Water Level: {water_level}")
                
                if water_level < WATER_THRESHOLD:
                    print("Water sensor triggered. Turning Water Pump ON.")
                    send_command(ser_wroom, "water_pump_ON")
                else:
                    print("Water sensor clear. Turning Water Pump OFF.")
                    send_command(ser_wroom, "water_pump_OFF")
                
                if temperature > TEMP_THRESHOLD:
                    print(f"Temperature {temperature}°C is high. Turning Air Pump and Peltiers ON.")
                    send_command(ser_wroom, "airpump_ON")
                    send_command(ser_c3, "peltier1_ON")
                    send_command(ser_c3, "peltier2_ON")
                    send_command(ser_c3, "peltier3_ON")
                    send_command(ser_c3, "peltier4_ON")
                    send_command(ser_c3, "peltier5_ON")
                else:
                    print(f"Temperature {temperature}°C is normal. Turning Air Pump and Peltiers OFF.")
                    send_command(ser_wroom, "airpump_OFF")
                    send_command(ser_c3, "peltier1_OFF")
                    send_command(ser_c3, "peltier2_OFF")
                    send_command(ser_c3, "peltier3_OFF")
                    send_command(ser_c3, "peltier4_OFF")
                    send_command(ser_c3, "peltier5_OFF")

        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("Control system stopped by user.")
            break       
        time.sleep(2)

if __name__ == "__main__":
	main()
	r3_serial.close()
	wroom32_serial.close()
	c3_serial.close()
	print("Serial ports closed.")
