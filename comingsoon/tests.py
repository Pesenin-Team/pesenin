from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *


class TestComingSoon(TestCase):

    def test_queue_page_url_is_exist(self):
        response = Client().get('/comingsoon/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_queue_page_url_resolves(self):
        url = reverse('comingsoon:coming')
        self.assertEquals(resolve(url).func, coming)
