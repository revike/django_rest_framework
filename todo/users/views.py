from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import BasePermission, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import ToDoUser
from users.serializers import UserModelSerializerV1, UserModelSerializerV2


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class UserModelViewSet(ListModelMixin, RetrieveModelMixin,
                       UpdateModelMixin, GenericViewSet, CreateModelMixin):
    queryset = ToDoUser.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserModelSerializerV1
    # permission_classes = [CustomPermission]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserModelSerializerV2
        return UserModelSerializerV1

    @action(detail=True, methods=['GET'])
    def user_name(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'name': user.username})

    @action(detail=True, methods=['GET'])
    def user_email(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'email': user.email})
