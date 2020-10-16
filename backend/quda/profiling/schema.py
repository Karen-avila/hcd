from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
from .forms import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ProfilingRulesNode(DjangoObjectType):
    class Meta:
        model = ProfilingRules
class ProfilingRulesInput(DjangoInputObjectType):
    class Meta:
        model = ProfilingRules
###############################################
class ProfilingFileColumnNode(DjangoObjectType):
    class Meta:
        model = ProfilingFileColumn
class ProfilingFileColumnInput(DjangoInputObjectType):
    rules = graphene.Field(ProfilingRulesInput)
    class Meta:
        model = ProfilingFileColumn
###############################################
class ProfilingFileNode(DjangoObjectType):
    class Meta:
        model = ProfilingFile
class ProfilingFileInput(DjangoInputObjectType):
    cols = graphene.List(ProfilingFileColumnInput, required=True)
    class Meta:
        model = ProfilingFile
###############################################
class ProfilingNode(DjangoObjectType):
    status = graphene.String()
    class Meta:
        model = Profiling
    def resolve_status(self, info):
        return self.getStatus()
class SetProfilingMutation(graphene.Mutation):
    profiling = graphene.Field(ProfilingNode)
    class Input:
        files = graphene.List(ProfilingFileInput)
    def mutate(self, info, files):
        return SetProfilingMutation(profiling=Profiling().setProfiling(info, files))
class RunProfilingMutation(graphene.Mutation):
    profiling = graphene.Field(ProfilingNode)
    class Input:
        profilingid = graphene.ID()
    def mutate(self, info, profilingid):
        profiling = Profiling.objects.get(id=profilingid).runProfiling(info)
        return RunProfilingMutation(profiling=profiling)
#################################################################
#########   QUERYS   ############################################
#################################################################
class Query(object):
    pass
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    setProfiling = SetProfilingMutation.Field()
    runProfiling = RunProfilingMutation.Field()
    ###########################################
