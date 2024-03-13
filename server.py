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

# Start the server
def start_server(host='0.0.0.0', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected by {addr}")

    def send_audio():
        stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
        try:
            while True:
                data = stream.read(chunk)
                conn.sendall(data)
        finally:
            stream.stop_stream()
            stream.close()

    def receive_audio():
        stream = p.open(format=format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk)
        try:
            while True:
                data = conn.recv(chunk)
                stream.write(data)
        finally:
            stream.stop_stream()
            stream.close()

    threading.Thread(target=send_audio).start()
    threading.Thread(target=receive_audio).start()

if __name__ == "__main__":
    start_server()
