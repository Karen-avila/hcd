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

class Mutation(object):
    qudagetdirectory = DirectoryMutation.Field()
    #qudatest = CleaningMutation.Field()


