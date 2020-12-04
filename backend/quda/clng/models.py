from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File
from .modelsRules import *

VARS = {
    'model': 'Cleaning',
    'name': 'Cleaning',
    'plural': 'Cleaning',
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
    def getCleaningFiles(self):
        return CleaningFile.objects.filter(profiling=self)
    def checkIfTerminated(self):
        if not CleaningFile.objects.filter(cleaning=self, finalDateTime__isnull=True):
            return True
        return False
    def setCleaning(self, info, name, files):
        self.user = info.context.user
        self.name = name
        self.save()
        for file in files:
            orderedRules = file.pop('orderedRules')
            file['cleaning'] = self
            cleaningFile = CleaningFile.objects.create(**file)
            for orderedRule in orderedRules:
                columnsinRules = orderedRule.pop('columnsinRules')
                orderedRule['cleaningFile'] = cleaningFile
                cleaningFileOrderedRulesInColumns = CleaningFileOrderedRulesInColumns.objects.create(**orderedRule)
                columns = columnsinRules.pop('columns')
                for column in columns:
                    column['cleaningFile'] = cleaningFile
                    cleaningFileOrderedRulesInColumns.columns.add(CleaningFileColumn.objects.get_or_create(**column)[0])
                for key, value in columnsinRules.items():
                    value.pop('apply_rule')
                    contentType = ContentType.objects.get(app_label='clng', model=key.lower())
                    rule = contentType.model_class().objects.create(**value)
                    cleaningFileOrderedRulesInColumns.rules.add(
                        CleaningFileRule.objects.get_or_create(content_type=contentType, object_id=rule.pk, cleaningFile=cleaningFile)[0]
                    )
        return self
    def runCleaning(self):
        if not self.initialDateTime:
            self.initialDateTime = timezone.now()
            self.save()
        for cleaningFile in self.getCleaningFiles():
            cleaningFile.runCleaningFile()
    def setTerminate(self):
        if not self.finalDateTime:
            self.finalDateTime = timezone.now()
            self.save()
        return True


########################################################################################
########################################################################################
VARS = {
    'model': 'CleaningFile',
    'name': 'CleaningFile',
    'plural': 'CleaningFile',
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
    def getCleaningFileOrderedRulesInColumns(self):
        return CleaningFileOrderedRulesInColumns.objects.filter(cleaningFile=self).order_by('order')
    def runCleaningFile(self):
        #makeCleaningFile.delay(self.id)
        self.makeCleaningFile()
        return self
    def makeCleaningFile(self):
        self.initialDateTime = timezone.now()
        self.save()
        for cleaningFileOrderedRulesInColumns in self.getCleaningFileOrderedRulesInColumns():
            cleaningFileOrderedRulesInColumns.makecleaningFileOrderedRulesInColumns()
        self.finalDateTime = timezone.now()
        self.save()
        if self.cleaning.checkIfTerminated():
            self.cleaning.setTerminate()
        return self


########################################################################################
########################################################################################
VARS = {
    'model': 'CleaningFileOrderedRulesInColumns',
    'name': 'CleaningFileOrderedRulesInColumns',
    'plural': 'CleaningFileOrderedRulesInColumns',
}
class CleaningFileOrderedRulesInColumns(ModelBase):
    cleaningFile = models.ForeignKey('CleaningFile', on_delete=models.CASCADE, related_name='+', editable=False, help_text="")
    order = models.PositiveIntegerField()
    columns = models.ManyToManyField('CleaningFileColumn', blank=True)
    rules = models.ManyToManyField('CleaningFileRule', blank=True)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFileOrderedRulesInColumns {0}".format(self.id)
    def makecleaningFileOrderedRulesInColumns(self):
        file = self.cleaningFile.getFile(self.cleaningFile.filename, self.cleaningFile.sep, self.cleaningFile.encoding, self.cleaningFile.haveHeaders)
        for rule in self.rules.all():
            rule.applyInColumnFile(file, columns.all())


########################################################################################
########################################################################################
VARS = {
    'model': 'CleaningFileColumn',
    'name': 'CleaningFileColumn',
    'plural': 'CleaningFileColumn',
}
class CleaningFileColumn(File):
    cleaningFile = models.ForeignKey('CleaningFile', on_delete=models.CASCADE, related_name='+', editable=False, help_text="")
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
VARS = {
    'model': 'CleaningFileRule',
    'name': 'CleaningFileRule',
    'plural': 'CleaningFileRule',
}
class CleaningFileRule(File):
    cleaningFile = models.ForeignKey('CleaningFile', on_delete=models.CASCADE, related_name='+', editable=False, help_text="")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFileColumn {0}".format(self.id)
    def applyInColumnFile(self, file, columns):
        if self.cleaningFile.haveHeaders:
            file = file[1:]
        for row in file:
            for column in columns:
                row[column.index] = self.applyRule(row[column.index])
        return True
    def applyRule(self, value):
        return self.content_object.apply(value)
