from rest_framework.serializers import ModelSerializer

from main.models import Project, ToDo


class ProjectModelSerializer(ModelSerializer):
    """Сериализатор для Project"""
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    """Сериализатор для ToDo"""
    class Meta:
        model = ToDo
        fields = '__all__'
