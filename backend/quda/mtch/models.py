from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File
from django.utils import timezone

import pandas as pd
import jellyfish as jf
import recordlinkage as rl
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
########################################################################################
########################################################################################
VARS = {
    'model': 'Matching',
    'name': 'Match',
    'plural': 'Matchs',
}
class Matching(ModelBase):
    user = models.ForeignKey('core.User', null=True, on_delete=models.SET_NULL, related_name='+' )
    name = models.CharField(max_length=200, null=True, blank=True)
    extraField = models.CharField(max_length=500 ,null=True, blank=True, default='',help_text="extraField")
    extraField2 = models.CharField(max_length=500 ,null=True, blank=True, default='',help_text="extraField2")
    generalPunct = models.CharField(max_length=500 ,null=True, blank=True, default='',help_text="generalPunct")
    creationDateTime = models.DateTimeField( auto_now_add=True,  help_text="Fecha y hora de creacion de la configuracion del perfilamiento."    )
    initialDateTime = models.DateTimeField(null=True, blank=True, help_text="Fecha y hora de inicio de la ejecucion del proceso para el perfilamiento configurado.")
    finalDateTime = models.DateTimeField(null=True, blank=True, help_text="Fecha y hora de termino de la ejecucion del proceso para el perfilamiento configurado.")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "Match {0}".format(self.id)
    def setMatching(self, info, name,files,pareo,groupKey,extraField,extraField2,generalPunct,outputFile,reportField):
        self.user = info.context.user
        self.creationDateTime = timezone.now()
        self.name = name
        self.extraField = extraField
        self.extraField2 = extraField2
        self.generalPunct = generalPunct
        self.save()
        for file in files:
            file['matching'] = self
            resMatchingFile = MatchingFile(**file)
            resMatchingFile.save()
        for par in pareo:
            par['matching'] = self
            resPareo = Pareo.objects.create(**par)
        for gk in groupKey:
            gk['matching'] = self
            resGroupKey = GroupKey.objects.create(**gk)
        for of in outputFile:
            of['matching'] = self
            resOutputFile = OutputFile.objects.create(**of)
        for rf in reportField:
            rf['matching'] = self
            resReportField = ReportField.objects.create(**rf)
        return self
    # Método principal de matching para un archivo.
    def cleanStr(self,value):
        return value.replace('[','').replace(']','').replace("'","").replace('"','')
    def cleanList(self,lista):
        temp=[]
        print(lista)
        for ele in lista:
            temp.append(ele.strip())
        return temp
    def runMatching(self,info):
        print(">>> :runMatching")
        self.initialDateTime = timezone.now()
        self.save()
        separador=','
        matchingFile=MatchingFile.objects.filter(matching=self)
        pareo=Pareo.objects.filter(matching=self)
        groupKey=GroupKey.objects.filter(matching=self)
        outputFile=OutputFile.objects.filter(matching=self)
        reportField=ReportField.objects.filter(matching=self)

        #archivoPareo,atributosPareo,atributosGrupoLlave,camposExtra,puntuacionGeneral,archivosSalida,atributosReportes
        for file in matchingFile:
            archivoPareo=file
        self.extraField = self.cleanList(self.cleanStr(self.extraField).split(separador) )
        for par in pareo:
            atributosPareo=par
        atributosPareo.campos =               self.cleanList(self.cleanStr(atributosPareo.campos).split(separador) )
        atributosPareo.puntuacionesMinimas =  self.cleanList(self.cleanStr(atributosPareo.puntuacionesMinimas).split(separador) )
        atributosPareo.metodosPareo =         self.cleanList(self.cleanStr(atributosPareo.metodosPareo).split(separador) )
        atributosPareo.ponderaciones =        self.cleanList(self.cleanStr(atributosPareo.ponderaciones).split(separador) )

        for gk in groupKey:
            atributosGrupoLlave=gk
        atributosGrupoLlave.campos =      self.cleanList(self.cleanStr(atributosGrupoLlave.campos).split(separador))
        atributosGrupoLlave.estrategia =  self.cleanList(self.cleanStr(atributosGrupoLlave.estrategia).split(separador))
        atributosGrupoLlave.posInicial =  self.cleanList(self.cleanStr(atributosGrupoLlave.posInicial).split(separador))
        atributosGrupoLlave.longitud =    self.cleanList(self.cleanStr(atributosGrupoLlave.longitud).split(separador))

        for of in outputFile:
            archivosSalida=of
        archivosSalida.archivoUnicos = self.cleanList(self.cleanStr(archivosSalida.archivoUnicos).split(separador))
        for rf in reportField:
            atributosReportes=rf

        # Creamos la instancia spark del proceso.
        instanciaSpark = self.createSparkInstance()
        # Registramos en Spark las funciones personalizadas.
        self.addUdfToSpark(instanciaSpark)
        # Leemos el archivo a comparar.
        dfMtchFile = File.getFile(self,archivoPareo.filename,archivoPareo.sep,archivoPareo.encoding,archivoPareo.haveHeaders)
        # Convertimos el índice del DataFrame del archivo en columna.
        print(dfMtchFile[:5])
        dfMtchFile = self.indexToColumn(dfMtchFile)
        print(dfMtchFile[:5])
        # Convertimos el DataFrame pandas del archivo a DataFrame Spark y creamos su tabla temporal.
        dfMtchFile = instanciaSpark.createDataFrame(dfMtchFile.astype(str))
        dfMtchFile.createOrReplaceTempView("tmpMtchFile")
        # Reconstruimos el DataFrame del archivo con la llave grupal y con solo las columnas del reporte de similaridad.
        dfMtchFile = self.getColsGrupoLlave(instanciaSpark,atributosPareo.campos,atributosGrupoLlave.campos, \
                                            atributosGrupoLlave.estrategia,atributosGrupoLlave.posInicial, \
                                            atributosGrupoLlave.longitud,self.extraField,"tmpMtchFile")
        # Reconstruimos la tabla temporal del archivo.
        dfMtchFile.createOrReplaceTempView("tmpMtchFile")
        dfMtchFile.show()
        # Creamos el DataFrame para los registros similares (de Spark a Pandas).
        dfMtchSimi = dfMtchFile.toPandas()
        # Eliminamos el dataframe del archivo para liberar memoria.
        del dfMtchFile
        # Obtenemos los indices de los registros candidatos para la comparación.
        candidatos = self.getCandidatos(1,dfMtchSimi,None)
        # Obtenemos los registros similares y creamos su tabla temporal cuando hay registros a comparar.
        if len(candidatos) > 0:
            dfMtchSimi = self.getSimilares(1,dfMtchSimi,None,candidatos,atributosPareo,self.generalPunct,instanciaSpark)
            dfMtchSimi.createOrReplaceTempView("tmpMtchSimi")
            del dfMtchSimi # Eliminamos el dataframe pandas para liberar memoria.
            # Generamos el reporte de registros similares.

            df = self.makeRepSimilares(1,instanciaSpark,atributosPareo,self.extraField,None)
            df.show()
            # Exportamos el reporte de registros similares.
            self.exportFile(df,archivosSalida.rutaArchivos+archivosSalida.archivoSimilares,atributosReportes.fileType,atributosReportes.sep)
            # Generamos el reporte de registros únicos.
            df = self.makeRepUnicos(1,1,instanciaSpark,None)
        else:
            del dfMtchSimi # Eliminamos el dataframe pandas para liberar memoria.
            # Generamos el reporte de registros únicos.
            df = self.makeRepUnicos(0,1,instanciaSpark,None)
        # Exportamos el archivo de registros unicos.
        self.exportFile(df,archivosSalida.rutaArchivos+archivosSalida.archivoUnicos[0],atributosReportes.fileType, \
                        atributosReportes.sep)
        self.finalDateTime = timezone.now()
        self.save()
        return self
    # Método principal de matching para dos archivos.
    def runMatchingTwoFiles(self,info):
        #",archivoPareo1,archivoPareo2,atributosPareo,atributosGrupoLlave,camposExtra,camposExtraArchivo2,puntuacionGeneral,archivosSalida,atributosReportes)"
        #archivoPareo,atributosPareo,atributosGrupoLlave,camposExtra,puntuacionGeneral,archivosSalida,atributosReportes
        print(">>> :runMatching")
        self.initialDateTime = timezone.now()
        self.save()
        separador=','
        matchingFile=MatchingFile.objects.filter(matching=self)
        pareo=Pareo.objects.filter(matching=self)
        groupKey=GroupKey.objects.filter(matching=self)
        outputFile=OutputFile.objects.filter(matching=self)
        reportField=ReportField.objects.filter(matching=self)
        for idx,file in enumerate(sorted(matchingFile, key=lambda file: file.id)):
            if idx==0:
                archivoPareo1=file
            if idx==1:
                archivoPareo2=file

        self.extraField = self.cleanList(self.cleanStr(self.extraField).split(separador))
        self.extraField2 = self.cleanList(self.cleanStr(self.extraField2).split(separador))

        for par in pareo:
            atributosPareo=par
        atributosPareo.campos              = self.cleanList(self.cleanStr( atributosPareo.campos ).split(separador))
        atributosPareo.camposArchivo2      = self.cleanList(self.cleanStr( atributosPareo.camposArchivo2 ).split(separador))
        atributosPareo.puntuacionesMinimas = self.cleanList(self.cleanStr( atributosPareo.puntuacionesMinimas ).split(separador))
        atributosPareo.metodosPareo        = self.cleanList(self.cleanStr( atributosPareo.metodosPareo ).split(separador))
        atributosPareo.ponderaciones       = self.cleanList(self.cleanStr( atributosPareo.ponderaciones ).split(separador))

        for gk in groupKey:
            atributosGrupoLlave=gk
        atributosGrupoLlave.campos          =self.cleanList(self.cleanStr( atributosGrupoLlave.campos ).split(separador))
        atributosGrupoLlave.camposArchivo2  =self.cleanList(self.cleanStr( atributosGrupoLlave.camposArchivo2 ).split(separador))
        atributosGrupoLlave.estrategia      =self.cleanList(self.cleanStr( atributosGrupoLlave.estrategia ).split(separador))
        atributosGrupoLlave.posInicial      =self.cleanList(self.cleanStr( atributosGrupoLlave.posInicial ).split(separador))
        atributosGrupoLlave.longitud        =self.cleanList(self.cleanStr( atributosGrupoLlave.longitud ).split(separador))

        for of in outputFile:
            archivosSalida=of
        archivosSalida.archivoUnicos =self.cleanList(self.cleanStr( archivosSalida.archivoUnicos ).split(separador))

        for rf in reportField:
            atributosReportes=rf

        self.initialDateTime = timezone.now()
        # Creamos la instancia spark del proceso.
        instanciaSpark = self.createSparkInstance()
        # Registramos en Spark las funciones personalizadas.
        self.addUdfToSpark(instanciaSpark)
        # Leemos los archivos a comparar.
        dfMtchFile1 = File.getFile(self,archivoPareo1.filename,archivoPareo1.sep,archivoPareo1.encoding,archivoPareo1.haveHeaders)
        dfMtchFile2 = File.getFile(self,archivoPareo2.filename,archivoPareo2.sep,archivoPareo2.encoding,archivoPareo2.haveHeaders)
        # Convertimos el índice de los DataFrames de los archivos en columna.
        dfMtchFile1 = self.indexToColumn(dfMtchFile1)
        dfMtchFile2 = self.indexToColumn(dfMtchFile2)
        # Convertimos el DataFrame pandas de los archivo a DataFrame Spark y creamos su tabla temporal correspondiente.
        dfMtchFile1 = instanciaSpark.createDataFrame(dfMtchFile1.astype(str))
        dfMtchFile1.createOrReplaceTempView("tmpMtchFile1")
        dfMtchFile2 = instanciaSpark.createDataFrame(dfMtchFile2.astype(str))
        dfMtchFile2.createOrReplaceTempView("tmpMtchFile2")
        # Reconstruimos el DataFrame de los archivos con la llave grupal y con solo las columnas del reporte de similaridad.
        dfMtchFile1 = self.getColsGrupoLlave(instanciaSpark,atributosPareo.campos,atributosGrupoLlave.campos, \
                                             atributosGrupoLlave.estrategia,atributosGrupoLlave.posInicial, \
                                             atributosGrupoLlave.longitud,self.extraField,"tmpMtchFile1")
        dfMtchFile2 = self.getColsGrupoLlave(instanciaSpark,atributosPareo.camposArchivo2,atributosGrupoLlave.camposArchivo2, \
                                             atributosGrupoLlave.estrategia,atributosGrupoLlave.posInicial, \
                                             atributosGrupoLlave.longitud,self.extraField2,"tmpMtchFile2")
        # Reconstruimos las tablas temporales de los archivos.
        dfMtchFile1.createOrReplaceTempView("tmpMtchFile1")
        dfMtchFile1.show()
        dfMtchFile2.createOrReplaceTempView("tmpMtchFile2")
        dfMtchFile2.show()
        # Creamos los DataFrames de los registros similares (de Spark a Pandas).
        dfMtchSimi1 = dfMtchFile1.toPandas()
        dfMtchSimi2 = dfMtchFile2.toPandas()
        # Eliminamos los dataframes de los archivos para liberar memoria.
        del dfMtchFile1, dfMtchFile2
        # Obtenemos los indices de los registros candidatos para la comparación.
        candidatos = self.getCandidatos(2,dfMtchSimi1,dfMtchSimi2)
        # Obtenemos los registros similares y creamos su tabla temporal cuando hay registros a comparar.
        accion = 1
        if len(candidatos) > 0:
            dfMtchSimi1 = self.getSimilares(2,dfMtchSimi1,dfMtchSimi2,candidatos,atributosPareo,self.generalPunct,instanciaSpark)
            dfMtchSimi1.createOrReplaceTempView("tmpMtchSimi")
            del dfMtchSimi1,dfMtchSimi2 # Eliminamos los dataframes pandas para liberar memoria.
            # Generamos los reportes de registros similares.
            df = self.makeRepSimilares(2,instanciaSpark,atributosPareo,self.extraField,self.extraField2)

            self.exportFile(df,archivosSalida.rutaArchivos+archivosSalida.archivoSimilares,atributosReportes.fileType, \
                            atributosReportes.sep)
        else:
            accion = 0
            # Eliminamos los dataframes pandas para liberar memoria.
            del dfMtchSimi1,dfMtchSimi2
        # Generamos el reporte de registros únicos.
        i = 0
        while i <= 1:
            df = self.makeRepUnicos(accion,2,instanciaSpark,str(i+1))
            self.exportFile(df,archivosSalida.rutaArchivos+archivosSalida.archivoUnicos[i],atributosReportes.fileType, \
                            atributosReportes.sep)
            i+=1
        self.finalDateTime = timezone.now()
        self.save()
        return self
    # Método para crear la instancia Spark
    def createSparkInstance(self):
        return SparkSession \
            .builder \
            .appName('Mtch') \
            .getOrCreate()
    # Método para registrar funciones personalizadas en Spark.
    def addUdfToSpark(self,sparkInstance):
        sparkInstance.udf.register("udf_nysiis", lambda x: jf.nysiis(x))
        sparkInstance.udf.register("udf_metaphone", lambda x: jf.metaphone(x))
        sparkInstance.udf.register("udf_match_rating_codex", lambda x: jf.match_rating_codex(x))
    # Método para obtener la llave grupal para el pareo, y solo con las columnas para el reporte de similaridad.

    def getColsGrupoLlave(self,sparkInstance,camposPareo,camposGpoLlave,estrategia,posInicial,longitud,camposExtra,tabla):
        # Se arma la sentencia para generar la columna de la llave grupal.
        i, grupoLlave = 0, ''
        for columna in camposGpoLlave:
            if estrategia[i] == 'String':
                grupoLlave += 'substring(trim(' +  columna + '),' + str(posInicial[i]) + ',' + str(longitud[i]) + '),'
            elif estrategia[i] == 'Soundex':
                grupoLlave += 'soundex(trim(' +  columna + ')),'
            elif estrategia[i] == 'Nysiis':
                grupoLlave += 'udf_nysiis(trim(' +  columna + ')),'
            elif estrategia[i] == 'Metaphone':
                grupoLlave += 'udf_metaphone(trim(' +  columna + ')),'
            elif estrategia[i] == 'Match_Rating_Codex':
                grupoLlave += 'udf_match_rating_codex(trim(' +  columna + ')),'
            i+=1
        # Armamos la sentencia SELECT con la columna de GrpLlave, con las columnas de pareo, y las columnas extra.
        sentenciaSelect = "Level,concat(" + grupoLlave[0:len(grupoLlave)-1] + ") AS GrpLLave," + \
            ",".join(camposPareo) + "," + ",".join(camposExtra)
        # Retornamos el DataFrame con solo las columnas del pareo, la columna GrpLlave, y las columnas extra.
        return sparkInstance.sql("SELECT " + sentenciaSelect + " FROM " + tabla + " ORDER BY GrpLLave")
    # Método que convierte el indice del DataFrame en columna.
    def indexToColumn(self,df):
        # Convertimos el índice en columna.
        df.reset_index(inplace=True)
        # Renombramos el nombre de la columna creada.
        df.rename(columns={"index": "Level"}, inplace=True)
        # Reemplazamos los valores na de las columnas.
        df.fillna(value='',inplace=True)
        # Retornamos el DataFrame.
        return df
    # Método para generar obtener los candidatos para el proceso de pareo.
    def getCandidatos(self,numFiles,df1,df2):
        # Creamos un índice con pares de registros.
        metIndexer = rl.Index()
        metIndexer.block(left_on="GrpLLave", right_on="GrpLLave")
        # Retornamos el número de cruces para las comparaciones.
        if numFiles == 1:
            return metIndexer.index(df1)
        else:
            return metIndexer.index(df1,df2)
    # Método para obtener la similaridad de dos columnas a partir de su distancia.
    def distanceToSimilarity(self,resultadoPareo,lenColumnaL,lenColumnaR):
        if (lenColumnaL == 0 and lenColumnaR == 0):
            return 1.0
        elif (lenColumnaL >= lenColumnaR):
            return (lenColumnaL - resultadoPareo) / lenColumnaL
        else:
            return (lenColumnaR - resultadoPareo) / lenColumnaR
    # Método para obtener solamente los registros similares.
    def getSimilares(self,numFiles,df1,df2,candidatos,atributosPareo,generalPunct,sparkInstance):
        # Declaramos la lista que contendra los resultados del proceso.
        listaDatos = []
        # Agregamos a la lista de columnas el nombre de las columnas.
        listaColumnas = ['Level_M','Level_D'] # Nombre de las columnas que contiene los índices de los registros candidatos.
        for columna in atributosPareo.campos:
            listaColumnas.append('Score_' + columna) # Nombre de las columnas a comparar.
        listaColumnas += ['Weights','Score_General','Similares'] # Nombre de las columnas de peso y de puntuación general.
        # Obtenemos el número de columnas a comparar.
        numColumnas = len(atributosPareo.campos)
        # Realizamos la comparación entre columnas de acuerdo al método de pareo seleccionado.
        for indice in candidatos:
            # Declaramos las variables y las listas de trabajo.
            weight, score, puntMinima, listaPaso = 0, 0, 1, []
            # Agregamos a la lista de paso los índices de los registros a comparar (candidatos).
            listaPaso.append(df1.loc[indice[0]]['Level'])
            if numFiles == 1:
                listaPaso.append(df1.loc[indice[1]]['Level'])
            else:
                listaPaso.append(df2.loc[indice[1]]['Level'])
            # Realizamos la comparación y el cálculo del peso y de la puntuación general.
            for i in range(numColumnas):
                resultadoPareo = 0
                # Obtenemos del DataFrame ´los valores de las columnas.
                columnaL = df1.loc[indice[0]][atributosPareo.campos[i]].strip()
                if numFiles == 1:
                    columnaR = df1.loc[indice[1]][atributosPareo.campos[i]].strip()
                else:
                    columnaR = df2.loc[indice[1]][atributosPareo.camposArchivo2[i]].strip()
                # Obtenemos el método de pareo por aplicar.
                metodoPareo = atributosPareo.metodosPareo[i]
                # Realizamos la comparación de acuerdo al método de pareo seleccionado.
                if metodoPareo == 'jaro':
                    resultadoPareo = jf.jaro_similarity(columnaL,columnaR)
                elif metodoPareo == 'jarowinkler':
                    resultadoPareo = jf.jaro_winkler_similarity(columnaL,columnaR)
                elif metodoPareo == 'levenshtein':
                    resultadoPareo = self.distanceToSimilarity(jf.levenshtein_distance(columnaL,columnaR),len(columnaL),len(columnaR))
                elif metodoPareo == 'damerau_levenshtein':
                    resultadoPareo = self.distanceToSimilarity(jf.damerau_levenshtein_distance(columnaL,columnaR),len(columnaL),len(columnaR))
                elif metodoPareo == 'hamming':
                    resultadoPareo = self.distanceToSimilarity(jf.hamming_distance(columnaL,columnaR),len(columnaL),len(columnaR))
                elif metodoPareo == 'match_rating':
                    resultadoPareo = jf.match_rating_comparison(columnaL,columnaR)
                    if resultadoPareo == None:
                        resultadoPareo = 0.0
                    else:
                        resultadoPareo = float(resultadoPareo)
                # Calculamos el valor de las columnas Weight y Score.
                weight += resultadoPareo * (int(atributosPareo.ponderaciones[i]) / 100)
                score  += resultadoPareo
                # Agregamos a la lista de paso el resultado de la comparación.
                listaPaso += [f"{resultadoPareo:.3f}"]
                # Apagar la bandera cuando el resultado del pareo sea menor a la puntuación mínima del campo.
                if resultadoPareo < (int(atributosPareo.puntuacionesMinimas[i]) /100):
                    puntMinima = 0
            # Apagar la bandera cuando el peso sea menor a la puntuación general.
            if weight < (int(generalPunct)/100):
                puntMinima = 0
            # Agregamos a la lista de paso los resultados de las columnas Weights, Score, y PuntMin.
            listaPaso += [f"{weight:.3f}",f"{score/numColumnas:.3f}",puntMinima]
            # Agregamos los resultados a la lista de datos.
            listaDatos.append(listaPaso)
        # Retornamos en un DataFrame los resultados del Pareo ente columnas.
        return sparkInstance.createDataFrame(listaDatos, schema=listaColumnas)
    # Método que exporta los resultados en archivos.
    def exportFile(self,df,pathFile,typeFile,delimitador):
        cmdWrite = "df.repartition(1).write." + typeFile + "('" + pathFile + "',mode='overwrite',"
        if typeFile == 'csv':
            cmdWrite += "sep='" + delimitador + "',header=True,encoding=None)"
        elif typeFile == 'json':
            cmdWrite += "encoding=None)"
        elif typeFile in ('orc','parquet'):
            cmdWrite += "compression=None)"
        # Ejecutamos el comando de exportación del archivo.
        exec(cmdWrite)
    # Método para generar el reporte de registros únicos cuando no hay registros candidatos a comparar.
    def makeRepUnicos(self,accion,numFiles,instanciaSpark,fileDigit):
        # Armamos la sentencia SQL del reporte.
        sentenciaSel, nivel = "SELECT * FROM tmpMtchFile", 'b.Level_M'
        if accion == 0:
            if numFiles == 2:
                sentenciaSel += fileDigit
            sentencia2 = "ORDER BY Level"
        else:
            sentencia2 = "a WHERE NOT EXISTS(SELECT 1 FROM tmpMtchSimi b WHERE b.Similares == 1 AND "
            if numFiles == 1:
                sentencia2 += "b.Level_M == a.Level) AND NOT EXISTS(SELECT 1 FROM tmpMtchSimi b WHERE "+ \
                              "b.Similares == 1 AND b.Level_D == a.Level) ORDER BY a.Level"
            else:
                sentenciaSel += fileDigit
                if fileDigit == '2':
                    nivel = 'b.Level_D'
                sentencia2 += nivel + " == a.Level) ORDER BY a.Level"
        return instanciaSpark.sql(sentenciaSel + " " + sentencia2)
    # Método para generar el reporte de registros similares y el reporte de registros únicos.
    def makeRepSimilares(self,numFiles,instanciaSpark,atributosPareo,camposExtra,camposExtraArchivo2):
        # Declaramos las variables de trabajo.
        selectM, selectD = '',''
        if numFiles == 1:
            tblFile = "tmpMtchFile b, tmpMtchFile c "
            # Seleccionamos los campos de los registros del Master y del Detalle.
            for column in atributosPareo.campos:
                selectM += 'b.' + column + ' AS ' + column + '_M,'
                selectD += 'c.' + column + ' AS ' + column + '_D,'
            # Seleccionamos los campos extras a incluir en el reporte.
            for column in camposExtra:
                selectM += 'b.' + column + ' AS ' + column + '_M,'
                selectD += 'c.' + column + ' AS ' + column + '_D,'
        else:
            tblFile = "tmpMtchFile1 b, tmpMtchFile2 c "
            # Seleccionamos los campos de los registros del Master y del Detalle.
            for column in atributosPareo.campos:
                selectM += 'b.' + column + ' AS ' + column + '_M,'
            for column in atributosPareo.camposArchivo2:
                selectD += 'c.' + column + ' AS ' + column + '_D,'
            # Seleccionamos los campos extras a incluir en el reporte.
            for column in camposExtra:
                selectM += 'b.' + column + ' AS ' + column + '_M,'
            for column in camposExtraArchivo2:
                selectD += 'c.' + column + ' AS ' + column + '_D,'
        # Quitamos el caracter excedente de los campos del detalle (,)
        selectD = selectD[0:len(selectD)-1] + ' '
        # Armamos la sentencia SQL del reporte de registros similares.
        sentenciaSQL = "SELECT a.*,b.GrpLLave," + selectM + selectD + \
                       "FROM tmpMtchSimi a, " + tblFile + \
                       "WHERE a.Similares == 1 " + \
                       "AND b.Level == a.Level_M " + \
                       "AND c.Level == a.Level_D " + \
                       "ORDER BY a.Weights ASC"
        # Ejecutamos la consulta de registros similares.
        return instanciaSpark.sql(sentenciaSQL)

VARS = {
    'model': 'MatchingFile',
    'name': 'File',
    'plural': 'Files',
}
class MatchingFile(File):
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    initialDateTime = models.DateTimeField( null=True, blank=True, editable=False)
    finalDateTime = models.DateTimeField(null=True, blank=True, editable=False)
    dummy =  models.CharField(max_length=500 ,null=True, blank=True, default='',help_text="dummy")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)

VARS = {
    'model': 'Pareo',
    'name': 'Pareo_',
    'plural': 'Pareo_s',
}
class Pareo(ModelBase):
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    campos = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    camposArchivo2 = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    puntuacionesMinimas = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    metodosPareo = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    ponderaciones = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)

VARS = {
    'model': 'groupKey',
    'name': 'Grupo llave',
    'plural': 'Grupo llaves',
}
class GroupKey(ModelBase):
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    campos = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    camposArchivo2 = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    estrategia = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    posInicial = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    longitud = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)

VARS = {
    'model': 'OutputFile',
    'name': 'Archivo de salida',
    'plural': 'Archivos de salida',
}
class OutputFile(ModelBase):
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    rutaArchivos = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    archivoSimilares = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    archivoUnicos = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)

VARS = {
    'model': 'ReportField',
    'name': 'Atributo reporte',
    'plural': 'Atributos reporte',
}
class ReportField(ModelBase):
    matching = models.ForeignKey('Matching', on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    fileType = models.CharField(max_length=100 ,null=True, blank=True, default='',help_text="dummy")
    sep = models.CharField(max_length=1 ,null=True, blank=True, default='',help_text="dummy")
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
