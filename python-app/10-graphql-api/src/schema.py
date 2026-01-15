import graphene
from models import User as UserModel

class User(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    email = graphene.String()

class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User, id=graphene.Int(required=True))
    
    def resolve_users(self, info):
        return UserModel.get_all()
    
    def resolve_user(self, info, id):
        return UserModel.get_by_id(id)

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(User)
    
    def mutate(self, info, name, email):
        user = UserModel.create(name, email)
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
