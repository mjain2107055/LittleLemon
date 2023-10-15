from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_create_item(self):
        item1 = Menu.objects.create(
            title="IceCream", 
            price=80,
            inventory=100)
        self.assertEqual(item1.title, "IceCream")
        self.assertEqual(item1.price, 80)
        self.assertEqual(item1.inventory, 100)
        self.assertEqual(item1.description,"")
        
        