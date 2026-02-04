#!/usr/bin/env python3

from hello_helpers.hello_misc import HelloNode
import numpy as np


class StretchSequenceNode(HelloNode):
    def __init__(self):
        HelloNode.__init__(self)

    def run_sequence(self):
        """Execute the complete movement sequence"""

        # 1. Stow position
        self.get_logger().info('Moving to stow position...')
        self.move_to_pose({'joint_lift': 0.2, 'wrist_extension': 0.0})

        # 2. Move to full extension and height
        self.get_logger().info('Extending arm and lift...')
        self.move_to_pose({'wrist_extension': 0.5, 'joint_lift': 0.5})

        # 3. Move wrist joints one at a time
        self.get_logger().info('Moving wrist yaw...')
        self.move_to_pose({'joint_wrist_yaw': np.radians(30)})

        self.get_logger().info('Moving wrist pitch...')
        self.move_to_pose({'joint_wrist_pitch': np.radians(30)})

        self.get_logger().info('Moving wrist roll...')
        self.move_to_pose({'joint_wrist_roll': np.radians(30)})

        # 4. Open and close gripper
        self.get_logger().info('Opening gripper...')
        self.move_to_pose({'joint_gripper_finger_left': 50})

        self.get_logger().info('Closing gripper...')
        self.move_to_pose({'joint_gripper_finger_left': 0})

        # 5. Move head pan and tilt
        self.get_logger().info('Moving head pan...')
        self.move_to_pose({'joint_head_pan': np.radians(45)})

        self.get_logger().info('Moving head tilt...')
        self.move_to_pose({'joint_head_tilt': np.radians(45)})

        # 6. Stow again
        self.get_logger().info('Returning to stow position...')
        self.move_to_pose({'joint_lift': 0.2, 'wrist_extension': 0.0,
                          'joint_wrist_yaw': 0.0, 'joint_wrist_pitch': 0.0,
                          'joint_wrist_roll': 0.0})

        # 7. Move base forward 0.5m
        self.get_logger().info('Moving base forward 0.5m...')
        self.move_to_pose({'translate_mobile_base': 0.5})

        # 8. Rotate base 180 degrees
        self.get_logger().info('Rotating base 180 degrees...')
        self.move_to_pose({'rotate_mobile_base': np.radians(180)})

        # 9. Move base forward 0.5m again
        self.get_logger().info('Moving base forward 0.5m again...')
        self.move_to_pose({'translate_mobile_base': 0.5})

        self.get_logger().info('Sequence complete!')


def main():
    node = StretchSequenceNode.quick_create('stretch_sequence_node')
    node.run_sequence()


if __name__ == '__main__':
    main()
