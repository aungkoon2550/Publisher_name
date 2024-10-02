#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class Subsciber_News(Node):
    def __init__(self):                         # ทำการ add self เข้ามาใน class
        super().__init__("Subsciber_node")      # ทำการตั้งชื่อ node

        self.subscriber_ = self.create_subscription(String, "Email_Box", self.Callback_Subscriber, 10)
        self.get_logger().info("Node Subscriber Has been Strated!!")
    
    def Callback_Subscriber(self, msg):
        self.get_logger().info(str("Messages From Server :") + str(msg.data))


def main(args=None):
    rclpy.init(args=args)
    node = Subsciber_News()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()