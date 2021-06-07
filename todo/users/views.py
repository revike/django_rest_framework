from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, \
    RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import BasePermission, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import ToDoUser
from users.serializers import UserModelSerializer


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserModelViewSet(ListModelMixin, RetrieveModelMixin,
                       UpdateModelMixin, GenericViewSet, CreateModelMixin):
    queryset = ToDoUser.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [CustomPermission]

    @action(detail=True, methods=['GET'])
    def user_name(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'name': user.username})

    @action(detail=True, methods=['GET'])
    def user_email(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'email': user.email})
