#!/usr/bin/env python3
import serial
import pynmea2
import time

port = "/dev/ttyACM0"

def parseGPS(input_data):
	flag_parse = "GGA"
	if input_data.find(flag_parse) > 0:
		try:
			msg = pynmea2.parse(input_data)
			time_SYS = "%s:%s:%s" % (time.gmtime().tm_hour, time.gmtime().tm_min, time.gmtime().tm_sec)
			time_GPS = msg.timestamp
			posi_LAT = "%s%s" % ('-' if msg.lat_dir == "S" else '', msg.lat)
			posi_LON = "%s%s" % ('-' if msg.lon_dir == "W" else '', msg.lon)
			data_gps = (time_SYS, time_GPS, posi_LAT, posi_LON, msg.altitude, msg.altitude_units, msg.num_sats)
			print("SYS time: %s | GPS time: %s | Lat: %s | Lon: %s | Alt: %s %s | Sat: %s" % data_gps)
		except:
			print(input_data)


serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while True:
	input_data = serialPort.readline()
	input_data = input_data.decode('Ascii')
	parseGPS(input_data)
