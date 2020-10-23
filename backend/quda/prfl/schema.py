from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
from .forms import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ProfilingFileNode(DjangoObjectType):
    class Meta:
        model = ProfilingFile
class ProfilingFileInput(DjangoInputObjectType):
    class Meta:
        model = ProfilingFile

###############################################
class ProfilingNode(DjangoObjectType):
    getProfilingFiles = graphene.List(ProfilingFileNode)
    class Meta:
        model = Profiling
    def resolve_getProfilingFiles(root, info):
        return ProfilingFile.objects.filter(profiling=root)

#################################################################
#########   QUERYS   ############################################
#################################################################
class Query(object):
    pass

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    prflSetProfiling = graphene.Field(ProfilingNode,
        files = graphene.List(ProfilingFileInput)
    )
    def resolve_prflSetProfiling(self, info, files):
        return Profiling().setProfiling(info, files)
    ###########################################
    prflRunProfiling = graphene.Field(ProfilingNode,
        profilingid = graphene.ID()
    )
    def resolve_prflRunProfiling(self, info, profilingid):
        return Profiling.objects.get(id=profilingid).runProfiling()
