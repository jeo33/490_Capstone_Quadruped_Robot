import random
import socket
import time

# dummy functions
def read_sensor_data():
    data = []
    for it in range(0, 360):
        angle = random.uniform(8, 10)
        data.append(f"{it},{angle}")
    time.sleep(2)
    return data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  
server_socket.listen(1)
print("Waiting for connection...")

client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established.")

try:
    while True:
      
        data_str='start'
        client_socket.sendall(data_str.encode('utf-8'))
        data = read_sensor_data()

        data_str = "\n".join(data)
        client_socket.sendall(data_str.encode('utf-8'))
      
        data_str='end'
        client_socket.sendall(data_str.encode('utf-8'))
        time.sleep(1)
finally:
    client_socket.close()
    server_socket.close()
