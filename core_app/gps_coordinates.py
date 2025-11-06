import json
import os
import serial
import pynmea2
import platform
import time
import io
from dotenv import load_dotenv
from gps_Firebase_sender import FirebaseSender

load_dotenv()

serialPort = None
stream_source = None

systemType = platform.system()

try:
    sender = FirebaseSender(os.getenv("FIREBASE_PATH_NAME"), os.getenv("FIREBASE_DB_URL"))
    if systemType == "Linux":
        serialPort = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
        # noinspection PyTypeChecker
        stream_source = io.BufferedRWPair(serialPort, serialPort)
        while True:
            try:
                line = stream_source.readline()
                msg = pynmea2.parse(line)
                if msg.sentence_type == 'GGA':
                    if msg.gps_qual == 0:
                        continue
                #print(repr(msg))
                    data_to_send = {
                        "latitude": float(msg.latitude) if msg.latitude else 0.0,
                        "longitude": float(msg.longitude) if msg.longitude else 0.0,
                        "altitude": float(msg.altitude) if msg.altitude else 0.0,
                        "num_sats": int(msg.num_sats) if msg.num_sats else 0,
                        "timestamp_gps": f"{msg.timestamp}"  # Timestamp NMEA
                    }
                    sender.send_gps_data(data_to_send)
            except serial.SerialException as e:
                print('Device error: {}'.format(e))
    else:
        stream_source = open("../mock_gps_coordinates.txt", "r")
        for line in stream_source.readlines():
            try:
                msg = pynmea2.parse(line)
                if msg.sentence_type == 'GGA':
                    if msg.gps_qual == 0:
                        print("scartato msg per gps basso: "+msg.gps_qual)
                        continue
                #print(repr(msg))
                data_to_send = {
                    "latitude": float(msg.latitude) if msg.latitude else 0.0,
                    "longitude": float(msg.longitude) if msg.longitude else 0.0,
                    "altitude": float(msg.altitude) if msg.altitude else 0.0,
                    "num_sats": int(msg.num_sats) if msg.num_sats else 0,
                    "timestamp_gps": f"{msg.timestamp}"  # Timestamp NMEA
                }
                sender.send_gps_data(data_to_send)
                time.sleep(5)
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue
except Exception as e:
    print("Errore")
finally:
    if systemType == "Linux":
        serialPort.close()