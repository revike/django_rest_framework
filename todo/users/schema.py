from graphene import ObjectType, List, Schema, Field, Int, String, Mutation, ID
from graphene_django import DjangoObjectType

from main.models import ToDo, Project
from users.models import ToDoUser


class UserType(DjangoObjectType):
    class Meta:
        model = ToDoUser
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(ObjectType):
    all_users = List(UserType)
    all_todos = List(ToDoType)
    all_projects = List(ProjectType)
    user_id = Field(UserType, id_=Int(required=True))
    todo_by_user = List(ToDoType, name=String())

    def resolve_all_users(self, info):
        return ToDoUser.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_user_id(self, info, id_):
        return ToDoUser.objects.get(id=id_)

    def resolve_todo_by_user(self, info, name=None):
        if name:
            return ToDo.objects.all().filter(user__username=name)
        return ToDo.objects.all()


class UserUpdateMutation(Mutation):
    class Arguments:
        username = String(required=True)
        id_ = ID()

    user = Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, id_):
        user = ToDoUser.objects.get(id=id_)
        user.username = username
        user.save()
        return UserUpdateMutation(user)


class UserCreateMutation(Mutation):
    class Arguments:
        username = String(required=True)
        last_name = String(required=True)
        first_name = String(required=True)
        email = String(required=True)

    user = Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, last_name, first_name, email):
        user = ToDoUser(username=username, last_name=last_name,
                        first_name=first_name, email=email)
        user.save()
        return UserCreateMutation(user)


class Mutation(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()


schema = Schema(query=Query, mutation=Mutation)
