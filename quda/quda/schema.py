from core.schemaBase import *
from .models import *
from .forms import *

import os

############################################################
class DirectoryNode(graphene.ObjectType):
    structure = graphene.JSONString()
    class Meta:
        description = 'Regresa el directorio completo de archivos en una dirección'
    def get_structure(self, path):
        structure = {'name': os.path.basename(path)}
        if os.path.isdir(path):
            structure['type'] = "directory"
            structure['children'] = [self.get_structure(os.path.join(path,x)) for x in os.listdir(path)]
        else:
            structure['type'] = "file"
        return structure

class DirectoryMutation(graphene.Mutation):
    class Arguments:
        action = graphene.String(description="Se requiere para diferenciar los archivos necesarios para esa acción")
        user = graphene.ID()
    directory = graphene.Field(DirectoryNode)
    def mutate(self, info, **kwargs):
        directory = DirectoryNode()
        directory.structure = directory.get_structure('/app/temp/')
        return DirectoryMutation(directory=directory)
def holaMundo(self, info, **kwargs):
    directory = DirectoryNode()
    directory.structure = "{mensaje:'hola mundo'}"
    return DirectoryMutation(directory=directory)

############################################################

class Mutation(object):
    qudagetdirectory = DirectoryMutation.Field()
    qudadirectoryholaMundo = DirectoryMutation.Field(resolver=holaMundo)

