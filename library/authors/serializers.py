from rest_framework.serializers import HyperlinkedModelSerializer

from authors.models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer):
    """Сериализатор для Author"""
    class Meta:
        model = Author
        fields = '__all__'
