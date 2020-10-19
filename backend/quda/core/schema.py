from .schemaBase import *
from .models import *
from .forms import *
import graphql_jwt

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class SiteNode(DjangoObjectType):
    class Meta:
        model = Site

###############################################
class ModuleNode(DjangoObjectType):
    class Meta:
        model = Module

###############################################
class OrganizationNode(DjangoObjectType):
    class Meta:
        model = Organization

###############################################
class UserNode(BaseNode):
    class Meta:
        model = User
        interfaces = [graphene.relay.Node]
        connection_class = ConnectionBase

###############################################
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    coreuser = graphene.Field(UserNode)
    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(coreuser=info.context.user)

#################################################################
#########   QUERYS   ############################################
#################################################################
class CoreQuery(graphene.ObjectType):
    user = graphene.relay.Node.Field(UserNode)
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class AuthMutation(graphene.Mutation):
    kerberosAuth = ObtainJSONWebToken.Field()
    verifyToken = graphql_jwt.Verify.Field()
    ###########################################
    ###########################################
    def mutate(self, info, **kwargs):
        return AuthMutation(ObtainJSONWebToken(), graphql_jwt.Verify())

#################################################################
#########    SUBSCRIPTIONS    ###################################
#################################################################
class Subscription(object):
    hello = graphene.String()
    def resolve_hello(root, info):
        return Observable.interval(1000).map(lambda i: datetime.datetime.now())

    ###########################################

#################################################################
#########    SCHEMA    ##########################################
#################################################################
class Query(object):
    user = graphene.relay.Node.Field(UserNode)

class Mutation(object):
    auth = AuthMutation.Field()
