from .schemaBase import *
from .models import *
from .forms import *
import graphql_jwt

############################################################
class SiteNode(DjangoObjectType):
    class Meta:
        model = Site

############################################################
class ModuleNode(DjangoObjectType):
    class Meta:
        model = Module

############################################################
class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization

############################################################
class UserNode(BaseNode):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'username': ['exact', 'icontains', 'istartswith'],
            'email': ['exact', 'icontains', 'istartswith'],
            'visibleUsername': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (graphene.relay.Node, )
        connection_class = ConnectionBase
    @classmethod
    def get_queryset(cls, queryset, info):
        return cls.sortBy(queryset, info)

class UserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserNode)
    class Meta:
        form_class = UserForm

############################################################
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    coreuser = graphene.Field(UserNode)
    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(coreuser=info.context.user)

############################################################
######### QUERY & MUTATION & SUBSCRIPTION
############################################################
class Query(object):
    coreuser = graphene.relay.Node.Field(UserNode)

class Mutation(object):
    kerberosAuth = ObtainJSONWebToken.Field()
    verifyToken = graphql_jwt.Verify.Field()

class Subscription(object):
    hello = graphene.String()
    def resolve_hello(root, info):
        return Observable.interval(1000).map(lambda i: datetime.datetime.now())
