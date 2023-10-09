import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import matplotlib.pyplot as plt
import numpy as np

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.subscription = self.create_subscription(
            Int32,
            'sensor_data',  # Replace with the actual topic name
            self.callback,
            10)
        self.subscription

        # Initialize arrays to store data for plotting
        self.timestamps = []
        self.sensor_data = []

        # Create a Matplotlib figure and axis
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Sensor Data')
        self.line, = self.ax.plot([], [], 'b-', label='Sensor Data')
        self.ax.legend()

    def callback(self, msg):
        timestamp = rclpy.clock.Clock().now().to_msg().sec
        self.timestamps.append(timestamp)
        self.sensor_data.append(msg.data)

        # Update the plot with new data
        self.line.set_data(self.timestamps, self.sensor_data)
        self.ax.relim()
        self.ax.autoscale_view(True, True)
        self.fig.canvas.flush_events()

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

