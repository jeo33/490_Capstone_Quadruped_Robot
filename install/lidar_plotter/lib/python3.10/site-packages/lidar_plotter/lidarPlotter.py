import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32  # Use the appropriate message type

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.subscription = self.create_subscription(
            Int32,
            'sensor_data',  # Replace with the actual topic name
            self.callback,
            10)
        self.subscription  # Prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info('Received sensor data: %d' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    listener_node = ListenerNode()
    rclpy.spin(listener_node)
    listener_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

