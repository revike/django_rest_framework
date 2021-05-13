from rest_framework.serializers import HyperlinkedModelSerializer

from users.models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор для Author"""
    class Meta:
        model = User
        fields = '__all__'
