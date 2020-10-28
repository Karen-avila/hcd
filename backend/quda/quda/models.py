from quda.core.modelsBase import *
import pandas as pd
import csv
import os
import json

########################################################################################
########################################################################################
VARS = {
    'model': 'File',
    'name': 'Archivo',
    'plural': 'Archivos',
}
class File(ModelBase):
    filename = models.CharField(max_length=500, help_text="Nombre del archivo con 'path' completo")
    sep = models.CharField(max_length=1, default=',', help_text="Caracter utilizado como separador de los datos entre cada columna; ej. '^'")
    encoding = models.CharField(max_length=50, default='latin1', help_text="Metodo de codificación de caracteres; ej. 'latin1'")
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
    def getFile(self, filename, sep, encoding, header=True):
        if not filename:
            filename = self.filename
        if not sep:
            sep = self.sep
        if not encoding:
            encoding = self.encoding
        if not header:
            return pd.read_csv(filename, sep=sep, encoding=encoding, header=None)
        return pd.read_csv(filename, sep=sep, encoding=encoding)
    def getHeaders(self, filename, sep, encoding, header):
        return self.getFile(filename, sep, encoding, header).head()
    def getSamples(self, filename, sep, encoding, header):
        return self.getFile(filename, sep, encoding, header).sample(n=10, random_state=5).values.tolist()
