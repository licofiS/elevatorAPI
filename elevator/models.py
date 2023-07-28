# elevator/models.py

import time
from django.db import models

class Elevator(models.Model):
    OPERATIONAL = 'Operational'
    MAINTENANCE = 'Maintenance'
    STATUS_CHOICES = [
        (OPERATIONAL, 'Operational'),
        (MAINTENANCE, 'Maintenance'),
    ]

    current_floor = models.PositiveIntegerField(default=1)
    is_moving_up = models.BooleanField(default=False)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=OPERATIONAL
    )

    def __str__(self):
        return f"Elevator {self.pk}"

    def move_up(self):
        if self.status == Elevator.OPERATIONAL:
            if not self.is_moving_up:
                self.is_moving_up = True
                self.save()
                return True
        return False

    def move_down(self):
        if self.status == Elevator.OPERATIONAL:
            if self.is_moving_up:
                self.is_moving_up = False
                self.save()
                return True
        return False

    def open_door(self):
        if self.status == Elevator.OPERATIONAL:
            # For simulation, I assumed the door is opened for 2 seconds
            time.sleep(2)  # Simulate the door being opened for 2 seconds
            self.close_door()  # Close the door after 2 seconds
            return True
        return False

    def close_door(self):
        if self.status == Elevator.OPERATIONAL:
            # For simulation, I assumed the door is closed instantly
            return True
        return False

    def start_running(self):
        if self.status == Elevator.OPERATIONAL:
            # For simulation, I assumed the elevator is running after 2 seconds
            time.sleep(2)  # Simulate the elevator starting after 2 seconds
            return True
        return False

    def stop_running(self):
        if self.status == Elevator.OPERATIONAL:
            # For simulation, I assumed the elevator is stopped after 2 seconds
            time.sleep(2)  # Simulate the elevator stopping after 2 seconds
            return True
        return False