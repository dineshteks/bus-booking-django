from django.db import models

# Create your models here.
class TrainbookinginfoModel(models.Model):
    booking_id=models.CharField(max_length=20)
    source=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    journey_date=models.TextField(max_length=10)
    seats=models.TextField(max_length=100)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phoneno=models.CharField()
    amount=models.IntegerField()
    def __str__(self):
        return self.booking_id


