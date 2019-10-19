from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import *
from .models import *
# Create your tests here.


class TestQueue(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='username', password='password', email='username@test.com'
        )
        self.queue1 = Queue.objects.create(
            user=self.user,
            nama_makanan="Ayam mentega",
            status="Ready",
            foto="image.jpg"
        )

    def test_queue_page_url_is_exist(self):
        response = Client().get('/queue/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queue/index.html')

    def test_tambah_method_url_is_exist(self):
        response = Client().get('/queue/tambah/')
        self.assertNotEqual(response.status_code, 200)

    def test_search_page_url_is_exist(self):
        response = Client().get('/queue/search')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'queue/search.html')

    def test_queue_page_url_resolves(self):
        url = reverse('antrian:queue')
        self.assertEquals(resolve(url).func, antri)

    def test_search_method_resolves(self):
        url = reverse('antrian:tambah', args=[1])
        self.assertEquals(resolve(url).func, tambah_antrian)

    def test_search_page_resolves(self):
        url = reverse('antrian:search')
        self.assertEquals(resolve(url).func, search_antrian)

    def test_check_queue(self):
        jumlah = Queue.objects.all().count()
        self.assertEqual(jumlah, 1)

        name = "Ayam mentega"
        self.assertEqual(self.queue1.nama_makanan, name)

        foto = "Ready"
        self.assertEqual(self.queue1.status, foto)

        foto = "image.jpg"
        self.assertEqual(self.queue1.foto, foto)

        self.assertEqual(str(self.queue1), name)

    def test_queue_request(self):
        User = self.user
        self.assertEqual(self.queue1.user, User)
