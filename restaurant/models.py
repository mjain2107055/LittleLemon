from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    bookingDate = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'