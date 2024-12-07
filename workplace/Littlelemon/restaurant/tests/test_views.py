from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

class MenuViewTest(TestCase):
    def setup(self):
        self.menu1 = Menu.objects.create(name="Petit Déjeuner", price=5.50, inventory=25)
        self.menu2 = Menu.objects.create(name="Déjeuner", price=12.99, inventory=45)
        self.menu3 = Menu.objects.create(name="Dîner", price=20.00, inventory=99)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        response = self.client.get(reverse('menu-items'))

        self.assertEqual(response.data, serializer.data)
