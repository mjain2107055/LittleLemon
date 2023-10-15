from django.db import models

# Create your models here.
class booking_Model(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    reservation_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)
    
    def __str__(self) -> str:
        return self.first_name

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()
    description = models.CharField(max_length=1000, default="")
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
    
