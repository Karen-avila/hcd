from quda.core.schemaBase import *
from .models import *
from .forms import *

import os


class LogNode(graphene.ObjectType):
    get_log = graphene.String()
    def resolve_get_log(root, info):
        return "Soy el log"

############################################################
class DirectoryNode(graphene.ObjectType):
    get_structure = graphene.JSONString(
        path=graphene.String(default_value="/app/tmp/"),
        user=graphene.ID(default_value=""),
        action=graphene.String(default_value="")
    )
    get_hello = graphene.String()
    class Meta:
        description = 'Regresa el directorio completo de archivos en una dirección'
    def resolve_get_structure(root, info, path, user, action):
        files = []
        for x in os.listdir(path):
            structure = {'label': os.path.basename(x)}
            if os.path.isdir(path + x):
                structure['type'] = "directory"
            else:
                structure['type'] = "file"
            files.append(structure)
        return {'directory': files, 'path': path}
    def resolve_get_hello(root, info):
        return "Hola mundo"


class DirectoryMutation(graphene.Mutation):
    # class Arguments:
        # action = graphene.String(description="Se requiere para diferenciar los archivos necesarios para esa acción")
        # user = graphene.ID()
    directory = graphene.Field(DirectoryNode)
    log = graphene.Field(LogNode)
    def mutate(self, info, **kwargs):
        return DirectoryMutation(DirectoryNode(), LogNode())

############################################################
############################################################
############################################################
from pyspark.sql              import SparkSession
from pyspark.sql            import SQLContext

class CleaningNode(graphene.ObjectType):
    get_input_param = graphene.JSONString(
        parametros=graphene.String(default_value='{ "reglas":[{ "id": 100, "nombre": "parser nombre", "funcion": "PARSER NAME", "id_funcion": 100, "opc": null, "columna": [ "column_5" ] } ], "archivo": {    "id_archivo": 0,"ruta_src": "C:/Users/miguel.cruza/PycharmProjects/DQ_3/tmp/",    "ruta_tgt": "C:/Users/miguel.cruza/PycharmProjects/DQ_3/tmp/dev/la/lt_siais/",    "nombre": "PATRONES_TEMP_INC.txt",    "separador": "^",    "encabezado": false  }}')
        )
    class Meta:
        input_param  = 'Regresa los parametros de entrada de la Mutation'
        reglas_apply = 'Resumen log de reglas aplicadas'
        resume       = 'resumen general de proceso'
    def resolve_get_input_param(root,info, parametros):

        print("******** init resolve_get_input_param")
        spark = SparkSession.builder.master('spark://172.29.0.224:7070').appName("transf_data_pyspark_process").getOrCreate()
        print("********")
        print(spark)
        ruta_src         = parametros['archivo']['ruta_src']
        ruta_tgt         = parametros['archivo']['ruta_tgt']
        nom_src          = parametros['archivo']['nombre']
        archivo_src      = ruta_src + nom_src
        parametros.tabla = 'DF_TABLA'

        cleaning = CleaningNode()
        cleaning.input_param = input_param
        cleaning.input_param = lanch_process(input_param)
        return parametros
class CleaningMutation(graphene.Mutation):
    proceso = graphene.Field(CleaningNode)
    def mutate(self, info,**kwargs):
        return CleaningMutation(CleaningNode())


############################################################

class Mutation(object):
    qudagetdirectory = DirectoryMutation.Field()
    #qudatest = CleaningMutation.Field()


