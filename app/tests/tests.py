from django.urls import reverse
from app.models import Restaurant, Product, Profile
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestAll(APITestCase):
    register_url = reverse('sign-up')
    profile_url = reverse('profile-list')
    rating_url = reverse('ratings-list')
    restaurant_url = reverse('restaurants-list')
    product_url = reverse('products-list')
    wishlist_url = reverse('wishlist-list')

    def setUp(self):
        user_data = {'email': 'admin@hotmail.com',
                     'username': 'admin',
                     'password': '123'}
        login_url = reverse('login')
        self.user = User.objects.create_user(email='admin@hotmail.com', username='admin', password='123')

        self.login_response = self.client.post(login_url, user_data)
        self.token = self.login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        Restaurant.objects.create(name='Five Burger', link='qualquer link')
        self.response = self.client.get(self.restaurant_url)
        self.restaurant_id = self.response.data[0]['id']
        self.restaurant_detail = reverse('restaurants-detail', args=[self.restaurant_id])

        Product.objects.create(restaurant_id=Restaurant.objects.first().id,
                               name='Burger',
                               detail='Duplo',
                               price='R$ 54,99',
                               picture='')
        self.response = self.client.get(self.product_url)
        self.product_id = self.response.data[0]['id']
        self.product_detail = reverse('products-detail', args=[self.product_id])

        Profile.objects.create(username='vitor',
                               picture='')
        self.response = self.client.get(self.profile_url)
        self.profile_id = self.response.data[0]['id']
        self.profile_detail = reverse('profile-detail', args=[self.profile_id])

    def test_create_user(self):
        data = {'email': 'vitor@hotmail.com',
                'username': 'vitor',
                'password': '123'}
        response = self.client.post(self.register_url, data=data)

        self.assertEqual(response.status_code, 201)

    def test_create_restaurants(self):
        data = {'name': 'qualquer nome',
                'link': 'qualquer link',
                'picture': ''}
        response = self.client.post(self.restaurant_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])

    def test_list_restaurants(self):
        response = self.client.get(self.restaurant_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['name'], 'Five Burger')

    def test_edit_restaurants(self):
        data = {'name': 'qualquer nome',
                'link': 'novo link',
                'picture': ''}
        response = self.client.put(self.restaurant_detail, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['link'], data['link'])

    def test_delete_restaurants(self):
        response = self.client.delete(self.restaurant_detail)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_create_products(self):
        data = {'restaurant_id': Restaurant.objects.first().id,
                'name': 'Burger',
                'detail': 'Triplo',
                'price': 'R$ 54,99', }
        response = self.client.post(self.product_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['detail'], data['detail'])

    def test_list_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['detail'], 'Duplo')

    def test_edit_products(self):
        data = {'restaurant_id': Restaurant.objects.first().id,
                'name': 'Triplo Burger',
                'detail': 'Triplo',
                'price': 'R$ 54,99',
                'picture': ''}
        response = self.client.put(self.product_detail, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_products(self):
        response = self.client.delete(self.product_detail)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_create_profile(self):
        data = {'username': 'vitor123',
                'picture': ''}
        response = self.client.post(self.profile_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], data['username'])

    def test_list_profile(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['username'], 'vitor')

    def test_edit_profile(self):
        data = {'username': 'vitor321',
                'picture': ''}
        response = self.client.put(self.profile_detail, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], data['username'])

    def test_delete_profile(self):
        response = self.client.delete(self.profile_detail)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_create_ratings(self):
        data = {'product_id': Product.objects.first().id,
                'profile_id': Profile.objects.first().id,
                'product_rate': 5,
                'size': 4,
                'complement': 3,
                'side_dish': 3,
                'comment': 'muito bom, mas demorou pra entregar'}

        response = self.client.post(self.rating_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['size'], data['size'])
        self.response = self.client.get(self.rating_url)
        self.rating_id = self.response.data[0]['id']
        self.profile_detail = reverse('ratings-detail', args=[self.rating_id])
        return self.profile_detail

    def test_list_rating(self):
        response = self.client.get(self.rating_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_edit_rating(self):
        data = {'product_id': Product.objects.first().id,
                'profile_id': Profile.objects.first().id,
                'product_rate': 5,
                'size': 4,
                'complement': 3,
                'side_dish': 3,
                'comment': 'entregou rapido, mas muito ruim'}
        response = self.client.put(self.test_create_ratings(), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['comment'], data['comment'])

    def test_delete_rating(self):
        response = self.client.delete(self.test_create_ratings())
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)

    def test_create_wishlist(self):
        data = {'profile_id': Profile.objects.first().id,
                'product_id': Product.objects.first().id,
                'note': 'Quero pedir esse produto no final do mes'}
        response = self.client.post(self.wishlist_url, data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['note'], data['note'])
        self.response = self.client.get(self.wishlist_url)
        self.wishlist_id = self.response.data[0]['id']
        self.wishlist_detail = reverse('wishlist-detail', args=[self.wishlist_id])
        return self.wishlist_detail

    def test_list_wishlist(self):
        response = self.client.get(self.wishlist_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_edit_wishlist(self):
        data = {'profile_id': Profile.objects.first().id,
                'product_id': Product.objects.first().id,
                'note': 'Quero pedir esse produto no final de semana'}
        response = self.client.put(self.test_create_wishlist(), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['note'], data['note'])

    def test_delete_wishlist(self):
        response = self.client.delete(self.test_create_wishlist())
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, None)
