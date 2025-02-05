from wpilib import Talon, TimedRobot, Timer, run
from wpilib.drive import DifferentialDrive


class Robot(TimedRobot):
    """Robot that moves forward 30 seconds, then stops."""
    def __init__(self, duration: int = 30, speed: float = 0.5):
        """Initialize Robot"""
        super().__init__()
        self.left_drive = Talon(0)
        self.right_drive = Talon(1)
        self.drive = DifferentialDrive(self.left_drive, self.right_drive)
        self.drive_duration = duration
        self.speed = speed
        self.timer = Timer()

    def autonomousInit(self):
        """Start timer."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """Move forward for 30 seconds using periodic event loop."""
        if self.timer.get() < self.drive_duration:
            self.drive.tankDrive(self.speed, self.speed)
        else:
            self.drive.tankDrive(0, 0)


if __name__ == "__main__":
    run(Robot())
