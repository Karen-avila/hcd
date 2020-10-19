from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File
import csv
from django.utils import timezone


VARS = {
    'model': 'ProfilingRules',
    'name': 'Regla de perfilamiento',
    'plural': 'Reglas de perfilamiento',
}
class ProfilingRules(ModelBase):
    checkBlank = models.BooleanField(default=False)
    checkFloat = models.BooleanField(default=False)
    checkInt = models.BooleanField(default=False)
    checkDate = models.BooleanField(default=False)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Regla de perfilamiento: {0}".format(self.id)
    def ifIsBlank(self, value):
        if str(value).strip() == '':
            return True
        return False
########################################################################################
########################################################################################
VARS = {
    'model': 'Profiling',
    'name': 'Perfilamiento',
    'plural': 'Perfilamientos',
}
class Profiling(ModelBase):
    user = models.ForeignKey('core.User', null=True, on_delete=models.SET_NULL, related_name='+')
    creationDateTime = models.DateTimeField(auto_now_add=True)
    initialDateTime = models.DateTimeField(null=True, blank=True)
    finalDateTime = models.DateTimeField(null=True, blank=True)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Perfilamiento {0}".format(self.id)
    def setProfiling(self, info, files):
        self.user = info.context.user
        self.save()
        for file in files:
            file['profiling'] = self
            cols = file.pop('cols', None)
            profilingFile = ProfilingFile(**file)
            profilingFile.save()
            for col in cols:
                col['profilingFile'] = profilingFile
                profilingRules = ProfilingRules(**col.pop('rules', None))
                profilingRules.save()
                col['profilingRule'] = profilingRules
                profilingFileColumn = ProfilingFileColumn(**col)
                profilingFileColumn.save()
        return self
    def runProfiling(self):
        self.initialDateTime = timezone.now()
        self.save()
        for profilingFileColumn in ProfilingFileColumn.objects.filter(profilingFile__profiling=self):
            profilingFileColumn.runProfilingFileColumn()
        self.finalDateTime = timezone.now()
        self.save()
        return self
    def getStatus(self):
        status = 'inLine'
        if self.initialDateTime:
            status = 'processing'
        if self.finalDateTime:
            status = 'finished'
        return status
    def countsTypeOfDataFiles(self):
        for profilingFile in ProfilingFile.objects.filter(profiling=self):
            if self.getStatus() == 'inLine':
                profilingFile.countsTypeOfData()
        return ProfilingFile.objects.filter(profiling=self)
    def getFilesHeaders(self, pathFiles):
        headers = []
        for file in pathFiles.split(','):
            headers.append({
                'filename': file,
                'headers': ProfilingFile(files).getheader()
            })
        return {'header': headers }
########################################################################################
########################################################################################
VARS = {
    'model': 'ProfilingFile',
    'name': 'Archivo de Perfilamiento',
    'plural': 'Archivos de Perfilamiento',
}
class ProfilingFile(File):
    profiling = models.ForeignKey('Profiling', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    initialDateTime = models.DateTimeField( null=True, blank=True, editable=False)
    finalDateTime = models.DateTimeField(null=True, blank=True, editable=False)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def getStatus(self):
        status = 'inLine'
        if self.initialDateTime:
            status = 'processing'
        if self.finalDateTime:
            status = 'finished'
        return status
    def countsTypeOfData(self):
        if self.getStatus() == 'inLine':
            self.update(initialDateTime = timezone.localtime())
            for i in range(self.getColums()):
                profilingFileColumn = ProfilingFileColumn(self, i, 1)
########################################################################################
########################################################################################
VARS = {
    'model': 'ProfilingFileColumn',
    'name': 'Columna de archivos de perfilamiento',
    'plural': 'Columnas de archivos de perfilamiento',
}
class ProfilingFileColumn(ModelBase):
    profilingFile = models.ForeignKey('ProfilingFile',
            on_delete=models.CASCADE,
            related_name='+',
            editable=False
        )
    profilingRule = models.ForeignKey('ProfilingRules',
            on_delete=models.PROTECT,
            related_name='+',
            editable=False
        )
    columnIndex = models.IntegerField(default=0)
    blanks = models.IntegerField(default=0)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def runProfilingFileColumn(self):
        file = self.profilingFile.getFile(
            filename = self.profilingFile.filename,
            newline = self.profilingFile.newline,
            encoding = self.profilingFile.encoding,
            delimiter = self.profilingFile.delimiter,
            quotechar = self.profilingFile.quotechar,
        )
        for row in file:
            if self.profilingRule.checkBlank:
                if self.profilingRule.ifIsBlank(row[self.columnIndex]):
                    self.blanks += 1
        self.save()

