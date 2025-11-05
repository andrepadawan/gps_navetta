import serial
import pynmea2
import platform
import time
import io


serialPort = None
stream_source = None

systemType = platform.system()

try:
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
                print(repr(msg))
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
                print(repr(msg))
                time.sleep(5)
            except pynmea2.ParseError as e:
                print('Parse error: {}'.format(e))
                continue
except Exception as e:
    print("Errore")
finally:
    serialPort.close()