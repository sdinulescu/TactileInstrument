import serial
import csv

import argparse
import random
import time

from pythonosc import udp_client

# SET UP OSC CLIENT
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=5005, help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

# SET UP SERIAL LISTENER
arduino_port = "/dev/cu.usbmodem106810401" #serial port of Teensy
baud = 9600 #arduino uno runs at 9600 baud

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        data = decoded_bytes.split(' ')
        client.send_message("/data", data)
        print(data)
    except:
        print("Keyboard Interrupt")
        break
    



