import serial
import csv

import argparse
import random
import time

from pythonosc import udp_client

NUM_TRIALS = 40

# SET UP OSC CLIENT
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8888, help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

with open('trainingdata.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    classIndex = 1
    trialIndex = 1
    for row in reader:
        data = []
        for col in row:
            if (col == "Letter"): 
                data.append(classIndex)
                trialIndex += 1
                if (trialIndex > NUM_TRIALS): 
                    classIndex += 1
                    trialIndex = 1
            else: 
                data.append(row[col])
        print(data)
        client.send_message("/add", data)

# while True:
#     try:
#         # ser_bytes = ser.readline()
#         # decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
#         # data = decoded_bytes.split(' ')
#         client.send_message("/data", data)
#         print(data)
#     except:
#         print("Keyboard Interrupt")
#         break
    



