from quda.core.schemaBase import *
from .models import *
from .forms import *
import os

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class FileNode(DjangoObjectType):
    class Meta:
        model = File

###############################################

#################################################################
#########   QUERYS   ############################################
#################################################################
# class QudaQuery(graphene.Query):
#     pass
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class QudaMutation(graphene.Mutation):
    qudaFileGetDirectory = graphene.JSONString(
        path=graphene.String(default_value="/app/temp/"),
        typeFile=graphene.String(default_value="local")
    )
    def resolve_qudaFileGetDirectory(self, info, path, typeFile):
        return File().getDirectory(path, typeFile)

    ###########################################
    qudaFileGetHeaders = graphene.List(graphene.String,
        filename=graphene.String(),
        newline=graphene.String(default_value=''),
        encoding=graphene.String(default_value='Latin1'),
        delimiter=graphene.String(default_value=','),
        quotechar=graphene.String(default_value=',')
    )
    def resolve_qudaFileGetHeaders(self, info, filename, newline, encoding, delimiter, quotechar):
        return File().getHeaders(filename, newline, encoding, delimiter, quotechar)

    ###########################################
    ###########################################
    def mutate(self, info, **kwargs):
        return QudaMutation(
            qudaFileGetDirectory = qudaFileGetDirectory,
            qudaFileGetHeaders = qudaFileGetHeaders
        )

#################################################################
#########    SCHEMA    ##########################################
#################################################################
class Query(object):
    pass

class Mutation(object):
    quda = QudaMutation.Field()
