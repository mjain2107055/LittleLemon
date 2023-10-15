from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.booking_Model
        fields = '__all__'
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']