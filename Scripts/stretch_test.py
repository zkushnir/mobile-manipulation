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

