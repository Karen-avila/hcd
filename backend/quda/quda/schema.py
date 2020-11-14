from quda.core.schemaBase import *
from .models import *
from .forms import *
import os

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class FileNode(BaseNode):
    class Meta:
        model = File
        filter_fields = {
            'id': ['exact'],
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase

###############################################
class DataTypeNode(BaseNode):
    class Meta:
        model = DataType
        filter_fields = {
            'id': ['exact'],
            'isDefault': ['exact'],
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase

###############################################
class TypeHeaderFileNode(BaseNode):
    class Meta:
        model = TypeHeaderFile
        filter_fields = {
            'id': ['exact'],
        }
        interfaces = (graphene.relay.Node,)
        connection_class = ConnectionBase

class TypeHeaderFileInput(graphene.InputObjectType):
    dataType = graphene.ID(
        description = "Id de Tipo de Dato"
    ) ### REVISAR
    index = graphene.Int(
        default_value=",",
        description="Index del header al que se aplica el tipado"
    )
    headerName = graphene.String(
        description="Nombre del header al que se aplica el tipado"
    )

###############################################
class FileInput(graphene.InputObjectType):
    filename = graphene.String(
        required=True,
        description="Ruta absoluta donde se encuentra el archivo; ej. '/app/temp/file.csv'"
    )
    sep = graphene.String(
        default_value=",",
        description="Caracter utilizado como separador de los datos entre cada columna; ej. '^'"
    )
    encoding = graphene.String(
        default_value="latin1",
        description="Metodo de codificación de caracteres; ej. 'latin1'"
    )
    haveHeaders = graphene.Boolean(
        default_value=True,
        description="Tiene encabezados?"
    )
    datatypes = graphene.List(
        TypeHeaderFileInput,
        required=False,
        description="Tiene encabezados?"
    )
    class Meta:
        description = "Forma para leer un archivo CSV"

#################################################################
#########   QUERYS   ############################################
#################################################################
class Query(object):
    qudaDataTypeQuery = DjangoFilterConnectionField(DataTypeNode)

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
        haveHeaders=graphene.Boolean(default_value=True, description="Tiene encabezados?"),
        description = "Obtiene los encabezados de un archivo, se usa para saber si un archivo se lee de forma correcta."
    )
    def resolve_qudaFileGetHeaders(self, info, filename, sep, encoding, haveHeaders):
        return File().getHeaders(filename, sep, encoding, haveHeaders)

    ###########################################
    qudaFileGetSamples = graphene.List(
        graphene.List(graphene.String),
        filename=graphene.String(description="Ruta absoluta del archivo."),
        sep=graphene.String(default_value=",", description="Caracter separador del archivo"),
        encoding=graphene.String(default_value='Latin1', description="Codificación del archivo"),
        haveHeaders=graphene.Boolean(default_value=True, description="Tiene encabezados?"),
        description = "Obtiene las primeros N filas del archivo"
    )
    def resolve_qudaFileGetSamples(self, info, filename, sep, encoding, haveHeaders):
        return File().getSamples(filename, sep, encoding, haveHeaders)
