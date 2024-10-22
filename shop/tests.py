from django.test import TestCase
from shop.models import Item
from django.urls import reverse


class ItemTest(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            title='test item',
            description='test description',
            stock=3
        )

    def test_items_list(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test item')

    def test_item_count(self):
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(len(response.context['items']), 1)

    def test_no_items(self):
        Item.objects.all().delete() 
        response = self.client.get(reverse('shop:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No items available')  
