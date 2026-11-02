from django.shortcuts import render
from rest_framework.decorators import (api_view,permission_classes)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from .models import TrainbookinginfoModel
from .serializers import Trainserializer

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def getbookinginfo(request):
    if request.method =="GET":
        data=TrainbookinginfoModel.objects.all()
        serializer=Trainserializer(data,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        serializer=Trainserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"booked sucessfull"})
