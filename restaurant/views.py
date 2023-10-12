from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Booking,Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuItemSerializers, userSerializer
from rest_framework import status,viewsets
# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers
    
        
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
  
    
class UserViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = userSerializer(queryset, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
        
    