from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File
import csv
from django.utils import timezone

VARS = {
    'model': 'Cleaning',
    'name': 'Limpieza',
    'plural': 'Limpiezas',
}
class Cleaning(ModelBase):
    user = models.ForeignKey('core.User', null=True, on_delete=models.SET_NULL, related_name='+')
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Limpieza {0}".format(self.id)
########################################################################################
########################################################################################
