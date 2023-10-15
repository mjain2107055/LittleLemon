from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import booking_Model,Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuItemSerializers, userSerializer
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from .forms import BookingForm
from django.http import HttpResponse
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu" : menu_data}
    return render(request,'menu.html', main_data)

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def reservations(request):
    date = request.GET.get('date',datetime.today().date())
    bookings = booking_Model.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = booking_Model.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = booking_Model(
                first_name=data['first_name'],
                no_of_guest = data['no_of_guest'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date',datetime.today().date())

    bookings = booking_Model.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

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
    queryset = booking_Model.objects.all()
    serializer_class = BookingSerializer

class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = booking_Model.objects.all()
    serializer_class = BookingSerializer
    
class UserViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = userSerializer(queryset, many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
        
    