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

#################################################################
#########   QUERYS   ############################################
#################################################################
# class QudaQuery(graphene.Query):
#     pass
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class PrflMutation(graphene.Mutation):
    setProfiling = graphene.Field(ProfilingNode,
        files = graphene.List(ProfilingFileInput)
    )
    def resolve_setProfiling(self, info, files):
        return Profiling().setProfiling(info, files)

    ###########################################
    runProfiling = graphene.Field(ProfilingNode,
        profilingid = graphene.ID()
    )
    def resolve_runProfiling(self, info, profilingid):
        return Profiling.objects.get(id=profilingid).runProfiling()

    ###########################################
    ###########################################
    def mutate(self, info, **kwargs):
        return PrflMutation(
            runProfiling,
            setProfiling
        )

#################################################################
#########    SCHEMA    ##########################################
#################################################################
class Query(object):
    pass

class Mutation(object):
    prfl = PrflMutation.Field()