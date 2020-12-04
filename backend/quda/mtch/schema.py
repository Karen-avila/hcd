from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
#from .forms import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class MatchingFileInput(graphene.InputObjectType):
    filename = graphene.String( required=True,description="Ruta absoluta donde se encuentra el archivo; ej. '/app/temp/file.csv'")
    sep = graphene.String(default_value=",",description="Caracter utilizado como separador de los datos entre cada columna; ej. '^'")
    encoding = graphene.String(default_value="latin1",description="Metodo de codificación de caracteres; ej. 'latin1'")
    haveHeaders = graphene.Boolean(default_value=True,description="Indica si el archivo tiene o no tiene encabezados (True/False)")
    class Meta:
        description = "Forma para leer un archivo CSV"
###############################################
###############################################
class MatchingFieldsInput(graphene.InputObjectType):
    campos = graphene.List(graphene.String,required=True,description="Lista de campos.")
    puntuacionesMinimas = graphene.List(graphene.Int,required=True,description="Lista de puntuaciones mínimas por campo.")
    camposArchivo2 = graphene.List(graphene.String,null=True, blank=True, default='/',description="Lista de campos segundo archivo.")
    metodosPareo = graphene.List(graphene.String,required=True,description="Lista de métodos de pareo por campo.")
    ponderaciones = graphene.List(graphene.Int,required=True,description="Lista de ponderaciones por campo.")
    class Meta:
        description = "Atributos del pareo."
###############################################
###############################################
class MatchingFieldsTwoFilesInput(graphene.InputObjectType):
    campos = graphene.List(graphene.String,required=True,description="Lista de campos primer archivo.")
    camposArchivo2 = graphene.List(graphene.String,required=True,description="Lista de campos segundo archivo.")
    puntuacionesMinimas = graphene.List(graphene.Int,required=True,description="Lista de puntuaciones mínimas por campo.")
    metodosPareo = graphene.List(graphene.String,required=True,description="Lista de métodos de pareo por campo.")
    ponderaciones = graphene.List(graphene.Int,required=True,description="Lista de ponderaciones por campo.")
    class Meta:
        description = "Atributos del pareo."

###############################################
###############################################
class MatchingGpoLlaveInput(graphene.InputObjectType):
    campos = graphene.List(graphene.String,required=True,description="Lista de campos.")
    camposArchivo2 = graphene.List(graphene.String,null=True, blank=True, default='/',description="Lista de campos segundo archivo.")
    estrategia = graphene.List(graphene.String,required=True,description="Estrategia de agrupación por campo (String / Soundex).")
    posInicial = graphene.List(graphene.Int,required=True,description="Posiciones de inicio por campo (aplica solo para la estrategia String).")
    longitud = graphene.List(graphene.Int,required=True,description="Longitudes por campo (aplica solo para la estrategia String).")
    class Meta:
        description = "Atributos de la llave grupal."
###############################################
###############################################
class MatchingGpoLlaveTwoFilesInput(graphene.InputObjectType):
    campos = graphene.List(graphene.String,required=True,description="Lista de campos del primer archivo.")
    camposArchivo2 = graphene.List(graphene.String,required=True,description="Lista de campos del segundo archivo.")
    estrategia = graphene.List(graphene.String,required=True,description="Estrategia de agrupación por campo (String / Soundex).")
    posInicial = graphene.List(graphene.Int,required=True,description="Posiciones de inicio por campo (aplica solo para la estrategia String).")
    longitud = graphene.List(graphene.Int,required=True,description="Longitudes por campo (aplica solo para la estrategia String).")
    class Meta:
        description = "Atributos de la llave grupal."
###############################################
###############################################
class MatchingWriteFileOutput(graphene.InputObjectType):
    fileType = graphene.String(required=True,default_value="csv",description="Tipo de archivo; ej. 'csv','json','orc','parquet'")
    sep = graphene.String(required=True,default_value=",",description="Caracter utilizado como separador de los datos entre cada columna; ej. '^'")
    class Meta:
        description = "Forma para escribir un archivo."
###############################################
###############################################
class MatchingNameFileOutput(graphene.InputObjectType):
    rutaArchivos = graphene.String(required=True,description="Ruta donde se almacenaran los archivos de salida.")
    archivoSimilares = graphene.String(required=True,description="Nombre del archivo de registros similares.")
    archivoUnicos = graphene.List(graphene.String,required=True,description="Listado de los archivos de registros únicos.")
    class Meta:
        description = "Ruta y nombre de los archivos de salida."

#################################################################
#########    SCHEMA    ##########################################
#################################################################
class MatchingNode(DjangoObjectType):
    class Meta:
        model = Matching
class SetMatchingMutation(graphene.Mutation):
    matching = graphene.Field(MatchingNode)
    class Input:
        name = graphene.String(description = "Nombre del matching")
        files = graphene.List(MatchingFileInput,required=True,description="Ruta absoluta donde se encuentra el o los archivo(s); ej. '/app/part-m-00000'")
        pareo = graphene.List(MatchingFieldsInput,required=True,description="Ruta absoluta donde se encuentra el o los archivo(s); ej. '/app/part-m-00000'")
        groupKey = graphene.List(MatchingGpoLlaveInput,required=True,description="Ruta absoluta donde se encuentra el o los archivo(s); ej. '/app/part-m-00000'")
        extraField = graphene.List(graphene.String,required=False, description="Lista de campos extra a incluir en el reporte de similaridad.")
        extraField2 = graphene.List(graphene.String,required=False, default_value='')
        generalPunct = graphene.Int(required=True,description="Puntuación general del pareo.")
        outputFile = graphene.List(MatchingNameFileOutput,required=True,description="Archivos de salida.")
        reportField = graphene.List(MatchingWriteFileOutput,required=True,description="Atributos de los archivos de salida.")
    def mutate(self,info,name,files,pareo,groupKey,extraField,extraField2,generalPunct,outputFile,reportField):
        return SetMatchingMutation(matching=Matching().setMatching(info,name,files,pareo,groupKey,extraField,extraField2,generalPunct,outputFile,reportField))

class RunMatchingMutation(graphene.Mutation):
    matching = graphene.Field(MatchingNode)
    class Input:
        matchingid = graphene.ID()
    def mutate(self,info,matchingid):
        matching = Matching.objects.get(id=matchingid).runMatching(info)
        return RunMatchingMutation(matching=matching)

class RunMatchingTwoFilesMutation(graphene.Mutation):
    matching = graphene.Field(MatchingNode)
    class Input:
        matchingid = graphene.ID()
    def mutate(self,info,matchingid):
        matching = Matching.objects.get(id=matchingid).runMatchingTwoFiles(info)
        return RunMatchingMutation(matching=matching)

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
    mtchSetMatching = SetMatchingMutation.Field(
        description = "Configuracion de limpieza de archivos para 1 o mas archivos")
    mtchRunMatching = RunMatchingMutation.Field(
        description="Ejecuta el proceso de pareo para un solo archivo."
    )
    mtchRunMatchingTwoFiles = RunMatchingTwoFilesMutation.Field(
        description="Ejecuta el proceso de pareo para un solo archivo."
    )

    ###########################################


    mtchRunMatchingTwoFiles2 = graphene.Field(MatchingNode,
        archivoPareo1 = graphene.List(MatchingFileInput,
            description="Primer archivo a comparar."
        ),
        archivoPareo2 = graphene.List(MatchingFileInput,
            description="Segundo archivo a comparar."
        ),
        atributosPareo = graphene.List(MatchingFieldsTwoFilesInput,
            required=True,
            description="Atributos del pareo."
        ),
        atributosGrupoLlave = graphene.List(MatchingGpoLlaveTwoFilesInput,
            required=True,
            description="Atributos de la llave grupal."
        ),
        camposExtra = graphene.List(graphene.String,
            required=False,
            description="Lista de campos extra del archivo 1 a incluir en el reporte de similaridad."
        ),
        camposExtraArchivo2 = graphene.List(graphene.String,
            required=False,
            description="Lista de campos extra del archivo 2 a incluir en el reporte de similaridad."
        ),
        puntuacionGeneral = graphene.Int(
            required=True,
            description="Puntuación general del pareo."
        ),
        archivosSalida = graphene.List(MatchingNameFileOutput,
            required=True,
            description="Archivos de salida."
        ),
        atributosReportes = graphene.List(MatchingWriteFileOutput,
            required=True,
            description="Propiedades o atributos de los archivos de salida."
        ),
        description="Ejecuta el proceso de pareo para dos archivos."
    )
    def resolve_mtchRunMatching(self,info,archivoPareo,atributosPareo,atributosGrupoLlave,camposExtra,puntuacionGeneral,
                                archivosSalida,atributosReportes):
        return Matching().runMatching(info,archivoPareo,atributosPareo,atributosGrupoLlave,
                                      puntuacionGeneral,archivosSalida,atributosReportes)

    def resolve_mtchRunMatchingTwoFiles(self,info,archivoPareo1,archivoPareo2,atributosPareo,
                                        camposExtra,camposExtraArchivo2,puntuacionGeneral,archivosSalida,atributosReportes):
        return Matching().runMatchingTwoFiles(info,archivoPareo1,archivoPareo2,atributosPareo,
                                              camposExtra,camposExtraArchivo2,puntuacionGeneral,archivosSalida,atributosReportes)
