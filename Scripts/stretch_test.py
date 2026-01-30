import time
import numpy as np
import stretch_body.robot

robot = stretch_body.robot.Robot()

try:
    robot.startup()

    if not robot.is_calibrated():
        print("Robot not calibrated. Run: stretch_robot_home.py (and wrist/gripper home if needed)")
        raise SystemExit(1)

    robot.stow()
    robot.push_command()
    robot.arm.wait_until_at_setpoint()
    robot.lift.wait_until_at_setpoint()

    robot.arm.move_to(0.5)
    robot.lift.move_to(0.5)
    robot.push_command()
    robot.arm.wait_until_at_setpoint()
    robot.lift.wait_until_at_setpoint()

    robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
    robot.push_command()
    time.sleep(2.0)

    robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
    robot.push_command()
    time.sleep(2.0)

    robot.end_of_arm.move_to('wrist_roll', np.radians(30))
    robot.push_command()
    time.sleep(2.0)

    robot.end_of_arm.move_to('stretch_gripper', 50)
    robot.push_command()
    time.sleep(2.0)

    robot.end_of_arm.move_to('stretch_gripper', 0)
    robot.push_command()
    time.sleep(2.0)

    robot.head.move_by('head_pan', np.radians(45))
    robot.push_command()
    time.sleep(2.0)

    robot.head.move_by('head_tilt', np.radians(45))
    robot.push_command()
    time.sleep(2.0)

    robot.stow()
    robot.push_command()
    robot.arm.wait_until_at_setpoint()
    robot.lift.wait_until_at_setpoint()

    # Base moves: use sleeps (or check base status), and they won't run if bump is active
    robot.base.translate_by(0.5)
    robot.push_command()
    time.sleep(5.0)

    robot.base.rotate_by(np.radians(180))
    robot.push_command()
    time.sleep(10.0)

    robot.base.translate_by(0.5)
    robot.push_command()
    time.sleep(5.0)

finally:
    robot.stop()
