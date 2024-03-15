import random
import socket
import time
from datetime import datetime
from os import path

from rplidar import RPLidar

BAUDRATE: int = 115200
TIMEOUT: int = 1
#dummy functions
def read_sensor_data():
    dev_path = "COM8"

    if path.exists(dev_path):
        lidar = RPLidar(port=dev_path, baudrate=BAUDRATE, timeout=TIMEOUT)
        try:
            # for val in lidar.iter_scans():
            temp = []
            val2 = ""
            lidar_val = lidar.iter_scans()
            # lidar.stop()
            # lidar.stop_motor()
            # lidar.disconnect()
            seven_data = []
            count = 0
            for val in lidar_val:
                # print(val)
                for i in val:
                    temp.append(i[1])
                    temp.append(i[2])
                # if count < 2:
                #     # seven_data.append(temp)
                #     count+=1
                # else:
                #     val2 = "".join(str(temp))
                #     print(val2)
                #     # time.sleep(2)
                #     return val2


            # ...
                val2 = "".join(str(temp))
                print(val2)
                return val2
                # print(val)
                # print(type(val))
                # return data
        except:
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
    else:
        print('[Error] Could not found device: {0}'.format(dev_path))
    # return data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)
print("Waiting for connection...")

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established.")

try:
    while True:

        data_str='start'
        client_socket.sendall(data_str.encode('utf-8'))
        data = read_sensor_data()

        data_str = str(data).replace('[','').replace(']','')
        client_socket.sendall(data_str.encode('utf-8'))

        data_str='end'
        client_socket.sendall(data_str.encode('utf-8'))
        # time.sleep(1)
finally:
    client_socket.close()
    server_socket.close()
