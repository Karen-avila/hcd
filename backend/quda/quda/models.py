from quda.core.modelsBase import *
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
    rows = models.IntegerField(default=0, editable=False)
    columns = models.IntegerField(default=0, editable=False)
    quotechar = models.CharField(max_length=1)
    newline = models.CharField(max_length=5, default='', blank=True)
    delimiter = models.CharField(max_length=1, default=',')
    encoding = models.CharField(max_length=50, default='latin1')
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "File: {0}".format(self.id)
    def getFile(self, filename, newline, encoding, delimiter, quotechar):
        with open(filename, 'r', newline=newline, encoding=encoding) as csvFile:
            return list(csv.reader(csvFile, delimiter=delimiter, quotechar=quotechar))
    def getDirectory(self, path, typeFile):
        files = []
        if typeFile == 'local':
            for x in os.listdir(path):
                dictionary = {'label': x}
                if os.path.isdir(path + x):
                    dictionary['type'] = "directory"
                else:
                    dictionary['type'] = "file"
                files.append(dictionary)
        if typeFile == 'hdfs':
            pass
        return {'directory':files, 'path': path, 'typeFile': typeFile}
    def getHeaders(self, filename, newline, encoding, delimiter, quote):
        return self.getFile(filename, newline, encoding, delimiter, quote)[0]
    def getColums(self):
        if not self.columns:
            self.columns = len(self.profilingFile.getFile()[0])
            self.save()
        return self.columns
    def getRows(self):
        if not self.rows:
            self.rows = len(self.profilingFile.getFile())
            self.save()
        return self.rows
########################################################################################
########################################################################################



