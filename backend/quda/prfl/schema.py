from quda.core.schemaBase import *
from quda.core.schema import UserNode
from quda.quda.schema import FileInput
from .models import *
from .forms import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ProfilingFileNode(BaseNode):
    class Meta:
        model = ProfilingFile
        description = "Layout del archivo de perfilamiento."


###############################################
class ProfilingNode(BaseNode):
    getProfilingFiles = graphene.List(ProfilingFileNode,
        source="getProfilingFiles",
        description="Layout de informacion sobre la configuracion y ejecucion del archivo de perfilamiento."
    )
    getLenFiles = graphene.Int(
        source="getLenFiles"
    )
    class Meta:
        filter_fields = {
            'id': ['exact', 'icontains', 'istartswith'],
            'user': ['exact'],
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase
        model = Profiling


#########   QUERYS   ############################################
#################################################################
class Query(object):
    prflProfilingQuery = DjangoFilterConnectionField(ProfilingNode)
    prflProfiling = graphene.relay.Node.Field(ProfilingNode)


#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    ###########################################
    prflSetProfiling = graphene.Field(ProfilingNode,
        files = graphene.List(FileInput),
        description = "Configura el perfilamiento a partir de 1 o mas archivos"
    )
    def resolve_prflSetProfiling(self, info, files):
        return Profiling().setProfiling(info, files)
    ###########################################
    prflRunProfiling = graphene.Field(ProfilingNode,
        profilingid = graphene.ID(),
        description = "Ejecuta el perfilamiento por cada uno de los archivos que tiene configurado"
    )
    def resolve_prflRunProfiling(self, info, profilingid):
        return Profiling.objects.get(id=profilingid).runProfiling()
