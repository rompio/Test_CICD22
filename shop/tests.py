from django.test import TestCase
from shop.models import Item
from django.urls import reverse

# Create your tests here.
class ItemTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title = 'test item',
            description = 'test description',
            stock = 3
        )
    def test_items_list(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'test item')