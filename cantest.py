import can
import time
import os
import RPi.GPIO as GPIO
import queue
from threading import Thread

#led = 22
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(led, GPIO.OUT)
#GPIO

os.system("sudo /sbin/ip link set can0 up type can bitrate 1000000")
print("Ready")

try:
	bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan_native')
except OSError:
	print('Cannot find PiCAN board')

try:
	f = open("test.txt", 'w')
	while True:
		message = bus.recv()
		print(message)
		message = str(message)
		f.write(message)
except KeyboardInterrupt:
	f.close()


