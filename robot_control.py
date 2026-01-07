#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import cv2
import numpy as np

class RobotControllerCV(Node):
    def __init__(self):
        super().__init__('robot_controller_cv')
        self.vel_publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.04, self.control_loop)
        self.point = None
        self.window_name = "Control Panel"
        self.get_logger().info("Control Node Started. Upper half = GO, Lower half = STOP.")

    def control_loop(self):
        # Tworzymy tło okna
        cv_image = np.zeros((512, 700, 3), np.uint8)
        # Linia środkowa
        cv2.line(cv_image, (0, 256), (700, 256), (255, 255, 255), 1)

        twist_msg = Twist()

        if self.point is not None:
            # Rysuj punkt kliknięcia
            cv2.circle(cv_image, self.point, 10, (0, 255, 0), -1)

            # LOGIKA STEROWANIA
            # Jeśli Y < 256 (górna połowa) -> JEDŹ
            if self.point[1] < 256:
                twist_msg.linear.x = 0.5
                cv2.putText(cv_image, "przod", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Jeśli Y > 256 (dolna połowa) -> STOP
            else:
                twist_msg.linear.x = -0.5
                cv2.putText(cv_image, "tyl", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            self.vel_publisher_.publish(twist_msg)

        cv2.imshow(self.window_name, cv_image)
        cv2.waitKey(1)
        cv2.setMouseCallback(self.window_name, self.mouse_callback)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x, y)

def main(args=None):
    rclpy.init(args=args)
    node = RobotControllerCV()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
