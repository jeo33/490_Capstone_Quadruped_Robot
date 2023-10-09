import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  # You can change the message type to match your sensor data type
import serial

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher = self.create_publisher(Int32, 'sensor_data', 10)
        self.serial_port = '/dev/serial0'  # This is the default UART port on Raspberry Pi
        self.baud_rate = 115200  # The baud rate of the TF Luna sensor
        self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=0.5)
        self.ycounter = 0

    def getSensorData(self):
        try:
            while True:
                byte_t = self.ser.read(1)
                if byte_t == b'\x59':
                    self.ycounter += 1
                    if self.ycounter == 2:
                        response = self.ser.read(6)
                        if len(response) == 6:
                            distance = response[0] + response[1] * 256
                            self.ycounter = 0
                            return distance
                        else:
                            self.ycounter = 0
                else:
                    self.ycounter = 0
        except KeyboardInterrupt:
            pass

    def publishSensorData(self):
        while rclpy.ok():
            distance = self.getSensorData()
            msg = Int32()
            msg.data = distance
            self.publisher.publish(msg)
            self.get_logger().info('Publishing sensor data: %d' % distance)

def main(args=None):
    rclpy.init(args=args)
    sensor_node = SensorNode()
    sensor_node.publishSensorData()
    rclpy.spin(sensor_node)
    sensor_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

