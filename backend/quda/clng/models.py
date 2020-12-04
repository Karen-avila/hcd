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
    name = models.CharField(max_length=200, null=True, blank=True)
    creationDateTime = models.DateTimeField(auto_now_add=True, help_text="")
    initialDateTime = models.DateTimeField(null=True, blank=True, help_text="")
    finalDateTime = models.DateTimeField(null=True, blank=True, help_text="")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Cleaning {0}".format(self.id)
    def setCleaning(self, info, name, files):
        self.user = info.context.user
        self.name = name
        self.save()
        for file in files:
            orderedRules = file.pop('orderedRules')
            file['cleaning'] = self
            cleaningFile = CleaningFile.objects.create(**file)
            for orderedRule in orderedRules:
                columnsinRules = cleaningFile.pop('columnsinRules')
                orderedRule['cleaningFile'] = cleaningFile
                cleaningFileOrderedRulesInColumns = CleaningFileOrderedRulesInColumns.create(**orderedRule)
                for column in columnsinRules.columns:
                    cleaningFileOrderedRulesInColumns.columns.add(CleaningFileColumn.create(**column))
        return self

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
    destinationFileName = models.CharField(max_length=200, null=True, blank=True, help_text="ruta destino donde se colocara el nuevo archivo con el resultado de las reglas.")
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
class CleaningFileOrderedRulesInColumns(ModelBase):
    cleaningFile = models.ForeignKey('CleaningFile', on_delete=models.CASCADE, related_name='+', null=True, blank=True, editable=False, help_text="")
    order = models.PositiveIntegerField()
    rules = models.ManyToManyField(ContentType, blank=True)
    columns = models.ManyToManyField('CleaningFileColumn', blank=True)
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
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=250, null=True, blank=True)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFileColumn {0}".format(self.id)

########################################################################################
########################################################################################
