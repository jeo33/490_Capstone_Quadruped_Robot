import socket
import pyaudio

# Server configuration
HOST = '192.168.246.13'  # Replace with the IP address of the server
PORT = 8000

# Initialize PyAudio
audio_format = pyaudio.paInt16
channels = 1
sample_rate = 44100
chunk_size = 1024
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=audio_format, channels=channels, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

try:
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("Connected to server")

    while True:
        # Read audio data from microphone
        data = stream.read(chunk_size)
        # Send audio data to server
        client_socket.sendall(data)
except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    print("Closing connection")
    client_socket.close()
    audio.terminate()

