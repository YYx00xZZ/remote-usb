import sys
if sys.version_info[0] >= 3:
    unicode = str
import serial
import io
import time
import threading
import logging
# ser = serial.Serial()
# ser.baudrate = 115200
# ser.port="/dev/ttyACM3"
connected = False
ser = serial.serial_for_url('socket://10.147.17.10:7777', timeout=None)
# ser2 = serial.serial_for_url('socket://localhost:7001', timeout=None)

# ser.open()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
# # sio2 = io.TextIOWrapper(io.BufferedRWPair(ser2, ser2))

# sio.write(unicode("hello\n"))
sio.flush() # it is buffering. required to get the data out *now*
# sio2.flush() # it is buffering. required to get the data out *now*

def handle_data(data):
    print(data)

def read_from_port(ser, name,label):
    logging.info("Thread %s: starting", name)
    global connected # = True
    # while not connected:
    if (ser.in_waiting>0):
        serin = ser.read()
        connected = True
        print(serin)
        while True:
            print(str(label))
            reading = ser.readline().decode()
            handle_data(reading)
            time.sleep(0.01)
    # if (ser.in_waiting>0): #if incoming bytes are waiting to be read from the serial input buffer
    #     data_str = ser.read(ser.in_waiting).decode('ascii') #read the bytes and convert from binary array to ASCII
    #     print(data_str, end='') #print the incoming string without putting a new-line ('\n') automatically after every print()
    # #Put the rest of your code you want here
    # time.sleep(0.01) # Optional: sleep 10 ms (0.01 sec) once per loop to let other threads on your PC run during this time.
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    while True:
        print('1',read_from_port())# ser.readline())
        # print('2\t',ser2.readline())
