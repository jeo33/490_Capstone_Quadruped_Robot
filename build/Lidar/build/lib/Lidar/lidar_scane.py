from typing import List, Optional
import serial
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Define the serial port and baud rate
serial_port = '/dev/serial0'  # This is the default UART port on Raspberry Pi
baud_rate = 115200  # The baud rate of the TF Luna sensor
ser = serial.Serial(serial_port, baud_rate, timeout=0.5)
ycounter = 0
byte_t = b'\x55'  # Changed from b'/55' to b'\x55'

def getScanner():
    global ycounter  # Need to specify that you want to use the global ycounter
    try:
        while True:
            byte_t = ser.read(1)
            if byte_t == b'\x59':
                ycounter += 1
                if ycounter == 2:
                    response = ser.read(6)
                    if len(response) == 6:
                        distance = response[0] + response[1] * 256  # Corrected distance calculation
                        ycounter = 0
                        ser.close()
                        return distance
                    else:
                        ycounter = 0
            else:
                ycounter = 0
    except KeyboardInterrupt:
        pass

class Writer(Node):
    def __init__(self, name):
        super().__init__(name)
        self.get_logger().info("message from %s" % name)
        self.pub_novel = self.create_publisher(String, "scan_distance", 10)
        self.timer_period = 1
        self.counter = 0
        self.timer = self.create_timer(self.timer_period, self.time_callback)
        self.distance = 0

    def time_callback(self):
        msg = String()
        self.distance = getScanner()
        msg.data = "scanner: distance %d cm." % self.distance
        self.pub_novel.publish(msg)
        self.get_logger().info("publish in Writer: %s" % msg.data)
        self.counter += 1

def main(args=None):
    rclpy.init(args=args)
    Lidar_Scan_node = Writer("lidar_scan")
    rclpy.spin(Lidar_Scan_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

