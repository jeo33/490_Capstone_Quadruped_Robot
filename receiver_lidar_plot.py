import socket
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

def receive_and_process_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # server's IP address

    fig, ax = plt.subplots()  # Initialize the plot outside the loop
    x_set = []
    y_set = []
    line, = ax.plot([], [], marker='o', linestyle='', color='b')  # Initialize an empty plot line

    try:
        collecting = False
        collected_data = []

        while True:
            data = client_socket.recv(32768).decode('utf-8')
            if not data:
                print("Disconnected from server")
                break

            if 'start' in data:
                collecting = True
                collected_data = []  # Reset collected data
                continue

            if 'end' in data and collecting:
                collecting = False
                if collected_data[0] != "None":
                    print("Received complete data between 'start' and 'end':")
                    print('*******\n{}\n*******'.format(''.join(collected_data)))
                    combined_string = ''.join(collected_data)
                    combined_string = combined_string[1:]
                    combined_string = combined_string.split(',')
                    x_set = []
                    y_set = []
                    for it in range(0, len(combined_string), 2):
                        x_set.append(np.cos(float(combined_string[it]) / 180 * np.pi) * float(combined_string[it+1])/1000)
                        y_set.append(np.sin(float(combined_string[it]) / 180 * np.pi) * float(combined_string[it+1])/1000)
                    line.set_xdata(x_set)  # Update the x data of the plot line
                    line.set_ydata(y_set)  # Update the y data of the plot line
                    ax.relim()
                    ax.autoscale_view()
                    plt.xlim(-6, 6)
                    plt.ylim(-6, 6)
                    plt.draw()  # Redraw the plot
                    plt.pause(0.01)  # Pause to allow the plot to update
                    collected_data = []  # Optionally clear collected data after processing

                    continue

            if collecting:
                collected_data.append(data)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()

receive_and_process_data()
