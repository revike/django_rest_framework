from mixer.auto import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, \
    APIClient, APITestCase

from backend.users.views import UserModelViewSet
from .models import ToDoUser


class TestUserViewSet(APITestCase):
    """Тест Users"""

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/v1/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/users/',
                               {'username': 'rev', 'first_name': 'rev',
                                'last_name': 'rev', 'email': 'mail@mail.ru'})
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/v1/users/',
                               {'username': 'rev', 'first_name': 'rev',
                                'last_name': 'rev', 'email': 'mail@mail.ru'})
        view = UserModelViewSet.as_view({'post': 'create'})
        admin = ToDoUser.objects.create_superuser('admin', 'admin@mail.ru',
                                                  password='qwerty')
        force_authenticate(request, admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = mixer.blend(ToDoUser)
        response = self.client.get(f'/api/v1/users/{user.id}/')
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    def test_post_create_admin1(self):
        client = APIClient()
        ToDoUser.objects.create_superuser('admin', 'admin@mail.ru',
                                          password='qwerty')
        client.login(username='admin', password='qwerty')
        response = client.post('/api/v1/users/',
                               {'username': 'rev', 'first_name': 'rev',
                                'last_name': 'rev', 'email': 'mail@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()
        response = client.post('/api/v1/users/',
                               {'username': 'rev', 'first_name': 'rev',
                                'last_name': 'rev', 'email': 'mail@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
