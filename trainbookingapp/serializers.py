from rest_framework import serializers
from .models import TrainbookinginfoModel
class Trainserializer(serializers.ModelSerializer):
    class Meta:
        model=TrainbookinginfoModel
        fields="__all__"