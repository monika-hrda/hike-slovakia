from django.test import TestCase


class TestViews(TestCase):

    def test_all_hikes_view(self):
        """ Test view all_hikes """
        response = self.client.get('/hikes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hikes/hikes.html')
