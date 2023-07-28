#elevator/serializers.py

from rest_framework import serializers
from .models import Elevator

class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ['current_floor', 'is_moving_up', 'status']
