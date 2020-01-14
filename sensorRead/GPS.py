import serial
import pynmea2
import time

port = "/dev/ttyACM0"

def parseGPS(input_data):
	flag_parse = "GGA"
	if input_data.find(flag_parse) > 0:
		msg = pynmea2.parse(input_data)
		time_computer = "%s %s %s" % (time.gmtime().tm_hour, time.gmtime().tm_min, time.gmtime().tm_sec)
		data_gps = (time_computer, msg.timestamp, msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, msg.altitude, msg.altitude_units, msg.num_sats)
		print("Computer time: %s | GPS time: %s | Lat: %s %s | Lon: %s %s | Alt: %s %s | Satellites: %s" % data_gps, end="\r")
		#print(input_data)
		#print(msg)

serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
	input_data = serialPort.readline()
	input_data = input_data.decode('Ascii')
	parseGPS(input_data)
