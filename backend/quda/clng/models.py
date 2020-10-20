from django.contrib.contenttypes.models import ContentType
from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File

class BaseRule(ModelBase):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    def __str__(self):
        return "BaseRule {0}".format(self.id)

class CleaningRules(ModelBase):
    content_type = models.ForeignKey('ContentType', on_delete=models.CASCADE)
    description = modles.TextField()
    name = modles.CharField(max_length=100)
    code = modles.CharField(max_length=10)
    def __str__(self):
        return "CleaningRules {0}".format(self.id)
    def initCleaningRules(self):
        #from .modelsRules import * as rules
        return True

########################################################################################
########################################################################################
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
