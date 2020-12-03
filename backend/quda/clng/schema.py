from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
from .forms import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class CleaningFileNode(BaseNode):
    getStatus = graphene.String(
        source="getStatus",
        description=""
    )
    class Meta:
        model = CleaningFile
        filter_fields = {
            'id': ['exact',],
        }
        description = ""
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase


###############################################
class CleaningNode(BaseNode):
    getCleaningFiles = graphene.List(CleaningFileNode,
        source="getCleaningFiles",
        description=""
    )
    getLenCleaningFiles = graphene.Int(
        source="getLenCleaningFiles",
        description=""
    )
    getStatus = graphene.String(
        source="getStatus",
        description=""
    )
    class Meta:
        model = Cleaning
        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'user__username': ['exact', 'icontains'],
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase


#################################################################
#########   QUERYS   ############################################
#################################################################
# class QudaQuery(graphene.Query):
#     pass
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class ClngMutation(graphene.Mutation):
    pass
    ###########################################
    ###########################################
    def mutate(self, info, **kwargs):
        return ClngMutation()

#################################################################
#########    SCHEMA    ##########################################
#################################################################
class Query(object):
    pass

class Mutation(object):
    clng = ClngMutation.Field()
