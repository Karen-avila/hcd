from django.contrib.contenttypes.models import ContentType
from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File

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
        return "Cleaning {0}".format(self.id)

########################################################################################
########################################################################################
VARS = {
    'model': 'CleaningFile',
    'name': 'Archivo de Limpieza',
    'plural': 'Archivos de limpieza',
}
class CleaningFile(File):
    cleaning = models.ForeignKey('Cleaning', on_delete=models.CASCADE, related_name='+', null=True, blank=True, editable=False, help_text="Referencia de integridad del perfilamiento con el archivo.")
    initialDateTime = models.DateTimeField( null=True, blank=True, editable=False , help_text="Fecha y hora de inicio de la ejecucion del procesamiento del archivo.")
    finalDateTime = models.DateTimeField(null=True, blank=True, editable=False, help_text="Fecha y hora de termino de la ejecucion del procesamiento del archivo.")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFile {0}".format(self.id)
########################################################################################
########################################################################################

VARS = {
    'model': 'CleaningRule',
    'name': 'CleaningRule',
    'plural': 'CleaningRule',
}
class CleaningRule(ModelBase):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningRule {0}".format(self.id)
########################################################################################
########################################################################################

VARS = {
    'model': 'CleaningFileColumn',
    'name': 'CleaningFileColumn',
    'plural': 'CleaningFileColumn',
}
class CleaningFileColumn(File):
    cleaningFile = models.ForeignKey('CleaningFile', on_delete=models.CASCADE, related_name='+', null=True, blank=True, editable=False, help_text="")
    cleaningRules = models.ManyToManyField(CleaningRule)
    index = models.PositiveIntegerField()
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFileColumn {0}".format(self.id)
########################################################################################
########################################################################################
