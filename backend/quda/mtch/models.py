from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings

VARS = {
    'model': 'Matching',
    'name': 'Pareo',
    'plural': 'Pareos',
}
class Matching(ModelBase):
    user = models.ForeignKey('core.User', null=True, on_delete=models.SET_NULL, related_name='+')
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Pareo {0}".format(self.id)
########################################################################################
########################################################################################
