from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, \
    RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import ToDoUser
from users.serializers import UserModelSerializer


class UserModelViewSet(ListModelMixin, RetrieveModelMixin,
                       UpdateModelMixin, GenericViewSet):
    queryset = ToDoUser.objects.all()
    serializer_class = UserModelSerializer

    @action(detail=True, methods=['GET'])
    def user_name(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'name': user.user_name})

    @action(detail=True, methods=['GET'])
    def user_email(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'email': user.email})
