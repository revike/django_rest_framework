from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import ToDoUser


class UserModelSerializerV1(HyperlinkedModelSerializer):
    """Сериализатор для User v1"""

    class Meta:
        model = ToDoUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UserModelSerializerV2(HyperlinkedModelSerializer):
    """Сериализатор для User v2"""

    class Meta:
        model = ToDoUser
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
            'is_superuser', 'is_staff'
        )
