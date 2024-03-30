from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer

# Create your views here.
@api_view(['POST'])
def create_data(request):
    serializer = MyModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)