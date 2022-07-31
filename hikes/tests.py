from django.test import TestCase
from django.shortcuts import reverse
from .models import Hike


class TestViews(TestCase):

    def setUp(self):
        self.hike = Hike.objects.create(
            difficulty=0,
            title='test hike A',
            description="Test description",
            price=100.00,
        )

    def test_all_hikes_view(self):
        """ Test view all_hikes """
        response = self.client.get('/hikes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hikes/hikes.html')

    def test_hike_detail_view(self):
        """ Test view all_hikes """
        response = self.client.get(reverse('hike_detail', args=[self.hike.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'hikes/hike_detail.html')
