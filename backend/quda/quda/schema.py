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
class Query(object):
    pass
    ###########################################

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    qudaFileGetDirectory = graphene.JSONString(
        path=graphene.String(default_value="/app/temp/"),
        typeFile=graphene.String(default_value="local")
    )
    def resolve_qudaFileGetDirectory(root, info, path, typeFile):
        return File().getDirectory(path, typeFile)
    ###########################################
    qudaFileGetHeaders = graphene.List(graphene.String,
        filename=graphene.String(),
        newline=graphene.String(default_value=''),
        encoding=graphene.String(default_value='Latin1'),
        delimiter=graphene.String(default_value=','),
        quotechar=graphene.String(default_value=',')
    )
    def resolve_qudaFileGetHeaders(root, info, filename, newline, encoding, delimiter, quotechar):
        return File().getHeaders(filename, newline, encoding, delimiter, quotechar)
