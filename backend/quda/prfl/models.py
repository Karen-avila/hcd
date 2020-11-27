from quda.core.modelsBase import *
from django.conf import settings
from quda.quda.models import File, TypeHeaderFile, DataType
from django.utils import timezone

from .tasks import makeProfiling

from pandas_profiling import ProfileReport
import pandas as pd

import json

########################################################################################
########################################################################################
VARS = {
    'model': 'Profiling',
    'name': 'Perfilamiento',
    'plural': 'Perfilamientos',
}
class Profiling(ModelBase):
    user = models.ForeignKey('core.User', null=True, on_delete=models.SET_NULL, related_name='+', help_text="Referencia de integridad con el usuario que configuro el perfilamiento.")
    name = models.CharField(max_length=200, null=True, blank=True)
    creationDateTime = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creacion de la configuracion del perfilamiento.")
    initialDateTime = models.DateTimeField(null=True, blank=True, help_text="Fecha y hora de inicio de la ejecucion del proceso para el perfilamiento configurado.")
    finalDateTime = models.DateTimeField(null=True, blank=True, help_text="Fecha y hora de termino de la ejecucion del proceso para el perfilamiento configurado.")
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
            datatypes = file.pop('datatypes')
            file['profiling'] = self
            profilingFile = ProfilingFile.objects.create(**file)
            for datatype in datatypes:
                datatype['file'] = profilingFile
                datatype['dataType'] = DataType().getBy64Id(datatype['dataType'])
                TypeHeaderFile.objects.create(**datatype)
        return self
    def runProfiling(self):
        if not self.initialDateTime:
            self.initialDateTime = timezone.now()
            self.save()
        for profilingFile in ProfilingFile.objects.filter(profiling=self):
            profilingFile.runProfilingFile()
        if not self.finalDateTime:
            self.finalDateTime = timezone.now()
            self.save()
        return self
    def getProfilingFiles(self):
        return ProfilingFile.objects.filter(profiling=self)
    def getLenProfilingFiles(self):
        return self.getProfilingFiles().count()
########################################################################################
########################################################################################
VARS = {
    'model': 'ProfilingFile',
    'name': 'Archivo de Perfilamiento',
    'plural': 'Archivos de Perfilamiento',
}
class ProfilingFile(File):
    profiling = models.ForeignKey('Profiling', on_delete=models.CASCADE, related_name='+', null=True, blank=True, editable=False, help_text="Referencia de integridad del perfilamiento con el archivo.")
    initialDateTime = models.DateTimeField( null=True, blank=True, editable=False , help_text="Fecha y hora de inicio de la ejecucion del procesamiento del archivo.")
    finalDateTime = models.DateTimeField(null=True, blank=True, editable=False, help_text="Fecha y hora de termino de la ejecucion del procesamiento del archivo.")
    analysis = models.TextField(null=True, blank=True, help_text="Informacion referente al tiempo de ejecucion y generacion del analisis del archivo.")
    table = models.TextField(null=True, blank=True)
    variables = models.TextField(null=True, blank=True, help_text="Informacion estadistica referente a las columnas del archivo analisado.")
    scatter = models.TextField(null=True, blank=True)
    correlations = models.TextField(null=True, blank=True, help_text="Informacion estadistica del a correlacion de 2 o mas columnas del archivo a analizar.")
    missing = models.TextField(null=True, blank=True, help_text="Informacion estadistica de los registros vacios o nulos por columna.")
    messages = models.TextField(null=True, blank=True, help_text="Mensajes informativos referente a la composicion estadistica de los datos de cada columna del archivo.")
    package = models.TextField(null=True, blank=True)
    sample = models.TextField(null=True, blank=True)
    duplicates = models.TextField(null=True, blank=True, help_text="Informacion estadistica de los registros duplicados por columna.")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def runProfilingFile(self):
        # if self.finalDateTime:
        # return self
        profilingFile = makeProfiling.delay(self.id)
        return self
    def makeProfiling(self):
        self.initialDateTime = timezone.now()
        self.save()
        df = self.getFile(self.filename, self.sep, self.encoding, self.haveHeaders)
        profile = ProfileReport(df, explorative=True, config_file="/app/config/pandas/pandasProfiling.yml")
        profiling = json.loads(profile.to_json())
        self.__dict__.update(**profiling) # REVISAR
        self.variables = json.dumps(self.variables, separators=(',', ':')) # REVISAR
        self.save()
        self.finalDateTime = timezone.now()
        self.save()
        # profile.to_file("/app" + str(self.id))
        return self
