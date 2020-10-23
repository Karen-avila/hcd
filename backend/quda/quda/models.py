from quda.core.modelsBase import *
import pandas as pd
import csv
import os

########################################################################################
########################################################################################
VARS = {
    'model': 'File',
    'name': 'Archivo',
    'plural': 'Archivos',
}
class File(ModelBase):
    filename = models.CharField(max_length=500, help_text="Nombre del archivo con 'path' completo")
    sep = models.CharField(max_length=1, default=',')
    encoding = models.CharField(max_length=50, default='latin1')
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "File: {0}".format(self.id)
    def getDirectory(self, path, typeFile):
        files = []
        for x in os.listdir(path):
            dictionary = {'label': x}
            if os.path.isdir(path + x):
                dictionary['type'] = "directory"
            else:
                dictionary['type'] = "file"
            files.append(dictionary)
        return {'directory':files, 'path': path, 'typeFile': typeFile}
    def getFile(self):
        return pd.read_csv(self.filename, sep=self.sep, encoding=self.encoding)
    def getHeaders(self, filename, sep, encoding):
        return self.getFile().head()
