from rest_framework.viewsets import ModelViewSet

from users.models import ToDoUser
from users.serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = ToDoUser.objects.all()
    serializer_class = UserModelSerializer
