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

#################################################################
#########    MUTATIONS    #######################################
#################################################################
class Mutation(object):
    qudaFileGetDirectory = graphene.JSONString(
        path=graphene.String(default_value="/app/temp/"),
        typeFile=graphene.String(default_value="local"),
        description = "Obtiene la lista del directorio con los archivos disponibles"
    )
    def resolve_qudaFileGetDirectory(self, info, path, typeFile):
        return File().getDirectory(path, typeFile)
    ###########################################
    qudaFileGetHeaders = graphene.List(graphene.String,
        filename=graphene.String(),
        sep=graphene.String(default_value=','),
        encoding=graphene.String(default_value='Latin1'),
        description = "Obtiene los headers de un archivo, se usa para saber si un archivo se lee de forma correcta"
    )
    def resolve_qudaFileGetHeaders(self, info, filename, sep, encoding,):
        return File().getHeaders(filename, sep, encoding)

