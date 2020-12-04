from quda.core.schemaBase import *
from quda.core.schema import UserNode
from quda.quda.schema import FileInput
from .models import *
from .schemaRules import ColumnsinRulesInput

#################################################################
#########   INPUTS   ############################################
#################################################################
class OrderedRulesInput(graphene.InputObjectType):
    columnsinRules = graphene.Field(ColumnsinRulesInput, required=False)
    order = graphene.Int()
    class Meta:
        description = ""

#################################################################
class CleaningFileInput(FileInput):
    destinationFileName = graphene.String()
    orderedRules = graphene.List(OrderedRulesInput, required=False)
    class Meta:
        description = ""

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

#################################################################
class CleaningNode(BaseNode):
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
class Query(object):
    pass

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    clngSetCleaning = graphene.Field(CleaningNode,
        name = graphene.String(description = "Nombre de la estandarizacion"),
        files = graphene.List(CleaningFileInput, description = "Coleccion de archivos que se estandarizaran"),
        description = "Configura la limpieza a partir de 1 o mas archivos"
    )
    def resolve_clngSetCleaning(self, info, name, files):
        return Cleaning.setCleaning(info, name, files)

