#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node

class MeuNo(Node):

    def __init__(self):
        super().__init__("primeiro_no")
        self.counter = 0
        self.create_timer(1.0, self.timer_callback)
        
    def timer_callback(self):
        self.get_logger().info("OLÁ!" + str(self.counter) )
        self.counter +=1
        
def main(args=None):
    rclpy.init(args=args)
    node=MeuNo()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()