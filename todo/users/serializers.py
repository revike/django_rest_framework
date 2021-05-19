from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import ToDoUser


class UserModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор для User"""
    class Meta:
        model = ToDoUser
        fields = ('id', 'user_name', 'first_name', 'last_name', 'email')
