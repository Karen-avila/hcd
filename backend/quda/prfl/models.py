from quda.core.modelsBase import *
from django.conf import settings
from quda.quda.models import File
from django.utils import timezone

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
            profilingFile = ProfilingFile(**file)
            profilingFile.save()
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
########################################################################################
########################################################################################
VARS = {
    'model': 'ProfilingFile',
    'name': 'Archivo de Perfilamiento',
    'plural': 'Archivos de Perfilamiento',
}
class ProfilingFile(File):
    profiling = models.ForeignKey('Profiling', on_delete=models.CASCADE, related_name='+', null=True, blank=True, editable=False)
    initialDateTime = models.DateTimeField( null=True, blank=True, editable=False)
    finalDateTime = models.DateTimeField(null=True, blank=True, editable=False)
    analysis = models.TextField(null=True, blank=True)
    table = models.TextField(null=True, blank=True)
    variables = models.TextField(null=True, blank=True)
    scatter = models.TextField(null=True, blank=True)
    correlations = models.TextField(null=True, blank=True)
    missing = models.TextField(null=True, blank=True)
    messages = models.TextField(null=True, blank=True)
    package = models.TextField(null=True, blank=True)
    sample = models.TextField(null=True, blank=True)
    duplicates = models.TextField(null=True, blank=True)
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def runProfilingFile(self):
        if self.finalDateTime:
            return self
        self.initialDateTime = timezone.now()
        self.save()
        self.makeProfiling()
        self.finalDateTime = timezone.now()
        self.save()
        return self
    def makeProfiling(self):
        df = self.getFile(self.filename, self.sep, self.encoding)
        profile = ProfileReport(df, explorative=True, config_file="/app/config/pandas/pandasProfiling.min.yaml")
        profiling = json.loads(profile.to_json())
        self.__dict__.update(**profiling)
        profile.to_file(str(self.id))
        return self
