import socket
import pyaudio
import wave
import threading

# Audio settings
chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100

# Initialize PyAudio
p = pyaudio.PyAudio()

# Connect to the server
def connect_to_server(host='server_ip_address', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    def send_audio():
        stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
        try:
            while True:
                data = stream.read(chunk)
                s.sendall(data)
        finally:
            stream.stop_stream()
            stream.close()

    def receive_audio():
        stream = p.open(format=format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)
        try:
            while True:
                data = s.recv(chunk)
                stream.write(data)
        finally:
            stream.stop_stream()
            stream.close()

    threading.Thread(target=send_audio).start()
    threading.Thread(target=receive_audio).start()

if __name__ == "__main__":
    connect_to_server()
