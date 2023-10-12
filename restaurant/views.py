from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Booking,Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuItemSerializers, userSerializer
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.``
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializers
    
        
class BookingView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = userSerializer(queryset, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
        
    