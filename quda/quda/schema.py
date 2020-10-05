from core.schemaBase import *
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
        path=graphene.String(default_value="/app/temp/"),
        user=graphene.ID(default_value=""),
        action=graphene.String(default_value="")
    )
    get_hello = graphene.String()
    class Meta:
        description = 'Regresa el directorio completo de archivos en una dirección'
    def resolve_get_structure(root, info, path, user, action):
        structure = {'name': os.path.basename(path)}
        if os.path.isdir(path):
            structure['type'] = "directory"
            structure['children'] = [root.resolve_get_structure(info, os.path.join(path,x, user, action), user, action) for x in os.listdir(path)]
        else:
            structure['type'] = "file"
        return structure
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
    #qudadirectoryholaMundo = DirectoryMutation.Field(resolver=holaMundo)

