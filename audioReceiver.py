import socket
import pyaudio
import numpy as np

#Server configuration listen to all
HOST = '0.0.0.0'
PORT = 8000

#Initialize PyAudio
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk_size = 1024
audio = pyaudio.PyAudio()

#Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Waiting for connection...")

#Accept incoming connection
client_socket, address = server_socket.accept()
print(f"Connection from {address} established")

#Open stream
stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, output=True, frames_per_buffer=chunk_size)

try:
    while True:
        # Receive audio data from client
        data = client_socket.recv(chunk_size)
        if not data:
            break
        audio_array = np.frombuffer(data, dtype = np.int16)
        amped = audio_array * 2
        amped_data = amped.tobytes()
        # Play received audio
        stream.write(amped_data)
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    print("Closing connection")
    client_socket.close()
    server_socket.close()
    audio.terminate()

