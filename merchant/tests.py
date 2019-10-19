from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client
from merchant.views import *
from merchant.models import *

class TestUrls(TestCase):
    def test_list_url_is_resolved(self):
        url = reverse('merchant:merchant')
        self.assertEquals(resolve(url).func, merchant)

    def test_list_url_is_resolved(self):
        url = reverse('merchant:makanan')
        self.assertEquals(resolve(url).func, makanan)

    def test_list_url_is_resolved(self):
        url = reverse('merchant:search_makanan')
        self.assertEquals(resolve(url).func, search_makanan)

    def test_list_url_is_resolved(self):
        url = reverse('merchant:search_merchant')
        self.assertEquals(resolve(url).func, search_merchant)

    def test_list_url_is_resolved(self):
        url = reverse('merchant:detail', args=[1])
        self.assertEquals(resolve(url).func, detail_makanan)
    
    def test_merchant_url_is_exist(self):
        response = Client().get('/merchant/')
        self.assertEqual(response.status_code, 200)

    def test_merchant_url_is_exist(self):
        response = Client().get('/merchant/makanan')
        self.assertEqual(response.status_code, 200)

    def test_merchant_url_is_exist(self):
        response = Client().get('/merchant/makanan/search_makanan')
        self.assertEqual(response.status_code, 200)

    def test_merchant_url_is_exist(self):
        response = Client().get('/merchant/search_merchant')
        self.assertEqual(response.status_code, 200)

    def test_create_merchant(self):
        self.merchant1 = Merchant.objects.create(
            nama_merchant = "Ayam Mentega",
            desc = "Ayam enak",
            link_gambar = "ayam.jpg"
        )
        jumlah = Merchant.objects.all().count()
        self.assertEqual(jumlah, 1)

        nama_merchant = "Ayam Mentega"
        self.assertEqual(self.merchant1.nama_merchant, "Ayam Mentega")

        desc = "Ayam enak"
        self.assertEqual(self.merchant1.desc, "Ayam enak")

        link_gambar = "ayam.jpg"
        self.assertEqual(self.merchant1.link_gambar, "ayam.jpg")
    
    def test_create_makanan(self):
        self.makanan1 = Makanan.objects.create(
            merchant = Merchant.objects.create(
                nama_merchant = "Ayam Mentega",
                desc = "Ayam enak",
                link_gambar = "ayam.jpg"
            ),
            nama = "Burger",
            deskripsi = "Roti",
            foto = "foto.jpg"
        )
        jumlah = Makanan.objects.all().count()
        self.assertEqual(jumlah, 1)

        nama = "Burger"
        self.assertEqual(self.makanan1.nama, "Burger")

        deskripsi = "Roti"
        self.assertEqual(self.makanan1.deskripsi, "Roti")

        foto = "foto.jpg"
        self.assertEqual(self.makanan1.foto, "foto.jpg")