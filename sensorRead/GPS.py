#!/usr/bin/env python3
import sys
import serial
import pynmea2
import time


def parseGPS(data):
	flag_parse = "GGA"
	if data.find(flag_parse) > 0:
		try:
			msg = pynmea2.parse(data)
			time_SYS = time.strftime('%Y%m%d-%H%M%S', time.localtime())
			time_GPS = msg.timestamp
			posi_LAT = "%s%s" % ('-' if msg.lat_dir == "S" else '', msg.lat)
			posi_LON = "%s%s" % ('-' if msg.lon_dir == "W" else '', msg.lon)
			data_gps = (time_SYS, time_GPS, posi_LAT, posi_LON, msg.altitude, msg.altitude_units, msg.num_sats)
			print("SYS time: %s | GPS time: %s | Lat: %s | Lon: %s | Alt: %s %s | Sat: %s" % data_gps)
		except:
			print(data)


if __name__ == "__main__":
	port = "/dev/ttyACM0"
	try:
		serialPort = serial.Serial(port, baudrate = 9600, timeout = 0.5)
		while True:
			data = serialPort.readline()
			data = data.decode('Ascii')
			parseGPS(data)
	except:
		print("No GPS module detected"); print(""); print("")
		sys.exit()
