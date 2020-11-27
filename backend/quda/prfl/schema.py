from quda.core.schemaBase import *
from quda.core.schema import UserNode
from quda.quda.schema import FileInput
from .models import *
from .forms import *

import base64

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ProfilingFileNode(BaseNode):
    class Meta:
        model = ProfilingFile
        filter_fields = {
            'id': ['exact',],
        }
        description = "Layout del archivo de perfilamiento."
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase


###############################################
class ProfilingNode(BaseNode):
    getProfilingFiles = graphene.List(ProfilingFileNode,
        source="getProfilingFiles",
        description="Layout de informacion sobre la configuracion y ejecucion del archivo de perfilamiento."
    )
    getLenProfilingFiles = graphene.Int(
        source="getLenProfilingFiles"
    )
    class Meta:
        model = Profiling
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
    prflProfilingQuery = DjangoFilterConnectionField(ProfilingNode)
    prflProfilingFileQuery = DjangoFilterConnectionField(ProfilingFileNode)
    prflProfilingFile = graphene.relay.Node.Field(ProfilingFileNode)


#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    prflSetProfiling = graphene.Field(ProfilingNode,
        name = graphene.String(description = "Nombre del perfilamiento"),
        files = graphene.List(FileInput, description = "Coleccion de archivos que se perfilarán"),
        description = "Configura el perfilamiento a partir de 1 o mas archivos"
    )
    def resolve_prflSetProfiling(self, info, name, files):
        return Profiling().setProfiling(info, name, files)
    ###########################################

    prflRunProfiling = graphene.Field(ProfilingNode,
        profilingid = graphene.ID(),
        description = "Ejecuta el perfilamiento por cada uno de los archivos que tiene configurado"
    )
    def resolve_prflRunProfiling(self, info, profilingid):
        return Profiling().getBy64Id(profilingid).runProfiling()
    ###########################################

    prflProfilingFileQuery = DjangoFilterConnectionField(ProfilingFileNode)
    prflProfilingFile = graphene.relay.Node.Field(ProfilingFileNode)


#################################################################
#########    SUBSCRIPTIONS    ###################################
#################################################################
class Subscription(graphene.ObjectType):
    prflProfiling = graphene.Field(ProfilingNode, id=graphene.ID())
    def resolve_prflProfiling(root, info, id):
        return root.filter(
            lambda event:
                event.operation == UPDATED and
                isinstance(event.instance, Profiling) and
                event.instance.pk == int(id)
        ).map(lambda event: event.instance)
