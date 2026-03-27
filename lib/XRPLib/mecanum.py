# XRPLib/mecanum.py
import math

class Mecanum:
    def __init__(self, motor1, motor2, motor3, motor4, imu):
        self.motor1 = motor1  # front right
        self.motor2 = motor2  # front left
        self.motor3 = motor3  # back right
        self.motor4 = motor4  # back left
        self.imu = imu

    def stop(self):
        self.motor1.set_effort(0)
        self.motor2.set_effort(0)
        self.motor3.set_effort(0)
        self.motor4.set_effort(0)

    def drive(self, x, y, rot, field_centric=True):
        forward = -x
        strafe = y
        rotate = rot

        if field_centric:
            yaw_degrees = self.imu.get_yaw()
            yaw_radians = yaw_degrees * math.pi / 180.0

            temp_forward = forward
            temp_strafe = strafe

            forward = temp_forward * math.cos(yaw_radians) + temp_strafe * math.sin(yaw_radians)
            strafe = -temp_forward * math.sin(yaw_radians) + temp_strafe * math.cos(yaw_radians)

        front_left = forward + strafe + rotate
        front_right = forward - strafe - rotate
        back_left = forward - strafe + rotate
        back_right = forward + strafe - rotate

        max_magnitude = max(
            abs(front_left),
            abs(front_right),
            abs(back_left),
            abs(back_right),
            1
        )

        front_left /= max_magnitude
        front_right /= max_magnitude
        back_left /= max_magnitude
        back_right /= max_magnitude

        self.motor1.set_effort(front_right)
        self.motor2.set_effort(front_left)
        self.motor3.set_effort(back_right)
        self.motor4.set_effort(back_left)