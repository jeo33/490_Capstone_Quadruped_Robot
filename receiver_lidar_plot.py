import socket
import matplotlib.pyplot as plt
import numpy as np


def receive_and_process_data():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('xxx.xxx.xxx.xxx', 12345))  # server's IP address 

    try:
        collecting = False  
        collected_data = []  

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print("Disconnected from server")
                break

            if 'start' in data:  # Check if the 'start' marker is in the received data
                collecting = True
                collected_data = []  # Reset collected data
                continue  # Skip the rest of this loop iteration

            if 'end' in data and collecting:  # Check if 'end' marker received and we're collecting
                collecting = False
                print("Received complete data between 'start' and 'end':")
                print('*******\n{}\n*******'.format(''.join(collected_data)))
                x_set=[]
                y_set=[]
                combined_string = ''.join(collected_data)
                combined_string=combined_string.split('\n')
                print(combined_string)
                for it in combined_string:
                    temp=it.split(',')
                    x_set.append(np.cos(int(temp[0])*180/np.pi)*float(temp[1]))
                    y_set.append(np.sin(int(temp[0])*180/np.pi)*float(temp[1]))
                #plot
                plt.figure(figsize=(10, 6))  # Create a new figure
                plt.plot(x_set, y_set, marker='o', linestyle='', color='b')  # Plot x_set vs y_set as dots
                plt.title('Received Data Plot')
                plt.xlabel('X Label')
                plt.ylabel('Y Label')
                plt.show()

                collected_data = []  # Optionally clear collected data after processing

                continue 

            if collecting:
                # If we're currently collecting, append the data (excluding 'start' and 'end' markers)
                collected_data.append(data)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        client_socket.close()


receive_and_process_data()
