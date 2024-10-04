from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Link, Product
from users.models import User


class LinkTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.pro')
        self.link = Link.objects.create(name='завод', email='ejik27@mail.ru', country="РФ", city="Москва",
                                        street="Сосновая", house_number="1", level="1", )
        self.client.force_authenticate(user=self.user)

    def test_link_retrieve(self):
        url = reverse('store:link_retrieve', args=(self.link.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.link.name
        )

    def test_link_create(self):
        url = reverse('store:link_create')
        data = {'name': 'завод', 'email': 'ejik27@mail.ru', 'country': 'РФ', 'city': 'Москва', 'street': 'Сосновая',
                'house_number': "1", 'level': '1'}

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Link.objects.all().count(), 2
        )

    def test_link_update(self):
        url = reverse('store:link_update', args=(self.link.pk,))
        data = {'name': 'Завод 1'}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data.get('name'), 'Завод 1'
        )

    def test_link_delete(self):
        url = reverse('store:link_delete', args=(self.link.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Link.objects.all().count(), 0
        )

    def test_link_list(self):
        url = reverse('store:link_list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@example.pro')
        self.link = Link.objects.create(name='завод', email='ejik27@mail.ru', country="РФ", city="Москва",
                                        street="Сосновая", house_number="1", level="1", )
        self.product = Product.objects.create(name='Телефон', product_model='15', release_date='2024-08-24',
                                              supplier=self.link)
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.product.name
        )

    def test_product_create(self):
        url = reverse('store:product-list')
        data = {'name': 'Ноутбук', 'product_model': '12', 'release_date': '2024-08-24', 'supplier': '1'}

        response = self.client.post(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Product.objects.all().count(), 2
        )

    def test_product_update(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        data = {'name': 'Пылесос'}
        response = self.client.patch(url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), "Пылесос"
        )

    def test_product_delete(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Product.objects.all().count(), 0
        )

    def test_product_list(self):
        url = reverse('store:product-list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
