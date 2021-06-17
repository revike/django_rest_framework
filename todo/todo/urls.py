"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from main.views import ProjectModelViewSet, ToDoModelViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='ToDo',
        default_version='1.0',
        description='Some description'
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/<str:version>/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),  # debug
    path('api-token-auth/', obtain_auth_token),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    re_path('^swagger(?P<format>\.json)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=False))),
]
