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
        description = "Orden de Reglas a aplicar"

#################################################################
class CleaningFileInput(FileInput):
    destinationFileName = graphene.String( description='Ruta donde se alojara el archivo transformado')
    orderedRules = graphene.List(OrderedRulesInput, required=False, description='Orden de ejecucion de las reglas')
    class Meta:
        only_fields = ('filename','sep','haveHeaders','destinationFileName','orderedRules',)
        description = "Agrega la configuracion de tus archivos"

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
        return Cleaning().setCleaning(info, name, files)

    clngRunCleaning = graphene.Field(CleaningNode,
        cleaningid = graphene.ID(),
        description = "Ejecuta la limpieza por cada uno de los archivos que tiene configurados"
    )
    def resolve_clngRunCleaning(self, info, cleaningid):
        return Cleaning().runCleaning(info,cleaningid)
