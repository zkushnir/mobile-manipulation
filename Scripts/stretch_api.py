import time
import numpy as np
import stretch_body.robot
robot = stretch_body.robot.Robot()
robot.startup()

robot.stow()
robot.push_command()
robot.arm.wait_until_at_setpoint()

# Move to full extension and height
robot.arm.move_to(0.5)
robot.lift.move_to(0.5)
robot.push_command()
robot.arm.wait_until_at_setpoint() # Wait for motion to complete

#move wrist joints one at a time
robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.end_of_arm.move_to('stretch_gripper', 50)
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.end_of_arm.move_to('stretch_gripper', 0)
robot.push_command()
robot.arm.wait_until_at_setpoint()

#move realsense
robot.head.move_by('head_pan', np.radians(45)) # Move head pan
robot.push_command()
robot.arm.wait_until_at_setpoint()
robot.head.move_by('head_tilt', np.radians(45)) # Move head tilt
robot.push_command()
robot.arm.wait_until_at_setpoint()

#stow all
robot.stow()
robot.push_command()
robot.arm.wait_until_at_setpoint()

