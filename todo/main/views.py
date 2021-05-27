from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from main.models import Project, ToDo
from main.serializers import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = PageNumberPagination
    pagination_class.default_limit = 10

    def get_queryset(self):
        name_project = self.request.query_params.get('name')
        if name_project:
            result = Project.objects.filter(name__contains=name_project)
            if result:
                return result
        return self.queryset


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = PageNumberPagination
    pagination_class.default_limit = 20

    def get_queryset(self):
        project_id = self.request.query_params.get('project')
        result = ToDo.objects.filter(project=project_id)
        if result:
            return result
        return ToDo.objects.all()

    def perform_destroy(self, instance):
        todo = ToDo.objects.get(id=instance.__dict__['id'])
        todo.is_active = False
        todo.save()
