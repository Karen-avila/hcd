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
        path=graphene.String(default_value="/app/temp/" , description = "Especificacion de la ruta para obtener los archivos del directorio; ej. '/app/temp/'"),
        typeFile=graphene.String(default_value="local", description = "Especificacion del rigen del archivo a analizar. ej. 'local'"),
        description = "Obtiene la lista del directorio con los archivos disponibles para el analisis."
    )
    def resolve_qudaFileGetDirectory(self, info, path, typeFile):
        return File().getDirectory(path, typeFile)
    ###########################################
    qudaFileGetHeaders = graphene.List(graphene.String,
        filename=graphene.String(description="Ruta absoluta del archivo."),
        sep=graphene.String(default_value=",", description="Caracter separador del archivo .csv entre cada columna ej. ','"),
        encoding=graphene.String(default_value='Latin1', description="Metodo de codificación de caracteres; ej. 'latin1'"),
        description = "Obtiene los encabezados de un archivo, se usa para saber si un archivo se lee de forma correcta."
    )
    def resolve_qudaFileGetHeaders(self, info, filename, sep, encoding,):
        return File().getHeaders(filename, sep, encoding)
