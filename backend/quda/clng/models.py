from quda.core.modelsBase import *
from graphql import GraphQLError
from django.conf import settings
from quda.quda.models import File
from .modelsRules import *

from django.utils import timezone
from pathlib import Path
from dateutil.parser  import parse
from datetime import datetime
import pyspark,os
from pyspark.sql  import SQLContext,SparkSession
from pyspark.sql.functions import current_date,unix_timestamp,to_date,lit,lower,upper,lpad,rpad,col,current_date,unix_timestamp,lit,regexp_replace,length,date_format,to_date,initcap,expr,substring,split
from pyspark.sql.types import BooleanType, DecimalType, IntegerType, StructField, StructType, StringType
from .udf import is_date,cadena_to_date2,fecha_proceso,parse_name


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
    def runCleaning(self,indo, cleaningid):
        if not self.initialDateTime:
            self.initialDateTime = timezone.now()
            self.save()
        clean=  Cleaning.objects.get(id=cleaningid)
        cleanFiles = CleaningFile.objects.filter(cleaning=clean)
        for file in cleanFiles:
            file.initProcess()
        self.finalDateTime = timezone.now()
        self.save()
        return self



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
    resultRules = models.TextField(null=True, blank=True)
    numBadLines = 0
    numTotalLines = 0
    lisBadLines = 0
    ds_conexion=''
    conf = None
    sc = None
    sqlCtx = None
    badDfPyspark = None
    dfPyspark = None
    tableDummy='TABLA'
    lisHeader=[]
    VARS = VARS
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def __str__(self):
        return "CleaningFile {0}".format(self.id)
    def recupera_duracion(self, fh_ini, fh_fin):
        if fh_ini and fh_fin:
            resultado = divmod( (datetime.strptime(str(fh_fin)[0:19],'%Y-%m-%d %H:%M:%S') -datetime.strptime(str(fh_ini)[0:19],'%Y-%m-%d %H:%M:%S')).total_seconds(),60)
            duracion = str(int(resultado[0]))+' min '+str(int(resultado[1]))+' seg'
            return duracion
        else:
            return '- min - seg'
    def log_dict(self):
       duracion = self.recupera_duracion(self.initialDateTime  , self.finalDateTime  )
       return {
                'archivo'  : self.filename,
                'lineas_malas':  { 'total_registros':self.numTotalLines,'cantidad': self.numBadLines ,'lineas': self.lisBadLines},
                'log' :  { 'inicio' :self.initialDateTime ,   'fin':self.finalDateTime, 'duracion': duracion },
                'reglas' :  self.reglas
                }
    def catchApplyRule(rule,total):
      ApplyRule={}
      ApplyRule['id'] = rule['id_rule']
      #ApplyRule['description'] = rule['description']
      #ApplyRule['name'] = rule['name']
      ApplyRule['total'] = total
      return ApplyRule
    ######################################################HELP  RULES
    ######################################################HELP  RULES
    def queryValidateLong(self, query):
        return self.sqlCtx.sql(query).collect()[0][0]
    def queryApplied(self, query, column,opc_bus=None):
      if opc_bus:
        return {"nombre":column,"busqueda":opc_bus,"aplicados":self.sqlCtx.sql(query).collect()[0][0]}
      else:
        return {"nombre":column,"aplicados":self.sqlCtx.sql(query).collect()[0][0]}
    def validateApplyChanges(self,datatype,table,column):
        dic={"nombre":column}
        if datatype=='date':
          query = "SELECT valida,count(valida) as valida_c from \
                   ( SELECT {c} as {c}, case when udf_is_date({c}) = 'false' then 'F' else 'V' end   as valida  FROM {t} ) \
                     group by valida".format(c=column,t=table,dt=datatype)
        else:
          query = "SELECT valida,count(valida) as valida_c from \
                   ( SELECT {c} as {c}, cast({c} as {dt}) as cast ,case when {c}=cast({c} as {dt}) then 'V' else 'F' end as valida  FROM {t} ) \
                     group by valida".format(c=column,t=table,dt=datatype)
        r = self.sqlCtx.sql(query)
        if r.count()==2:
            f = r.filter(r.valida == 'F').collect()[0][1]
            v = r.filter(r.valida == 'V').collect()[0][1]
            if f>v:
                return False, {"nombre":column,"aplicados":"0 No se puede aplicar regla por tipo de dato"}
            else:
              return True,dic
        elif r.count()==1:
            r2= r.filter(r.valida == 'F').collect()
            if (r2 and r2[0][0]=='F'):
                return False, {"nombre":column,"aplicados":"0 No se puede aplicar regla por tipo de dato"}
            else:
              return True,dic
        else:
            return True,dic
    ######################################################################## RULES
    ######################################################################## RULES
    def ruleLpad( self,column,rule, change):
        queryValidate = "SELECT max(length({c})) as {c} FROM {t}  ".format(c=column,t=self.tableDummy)
        valLong =self.queryValidateLong( queryValidate)
        if valLong <= rule['opc']['longitud']:
            queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE  length({c})<> {l}".format(c=column,l=rule['opc']['longitud'],t=self.tableDummy)
            applied = self.queryApplied( queryMetadata,column)
            if change:
                self.dfPyspark =self.dfPyspark.withColumn("{c}".format(c=column), lpad(col("{c}".format(c=column)),rule['opc']['longitud'],rule['opc']['caracter']) )
                self.dfPyspark.createOrReplaceTempView(self.tableDummy)
                return applied
            else:
                return applied
        else:
            print("no se puede realizar funcion cadena contiene mayor logitud")
            return {"nombre":column,"aplicados":0}

    def ruleRpad( self,column , rule, change):
        queryValidate = "SELECT max(length({c})) as {c} FROM {t} ".format(c=column,t=self.tableDummy)
        valLong = self.queryValidateLong(queryValidate)
        if valLong <= rule['opc']['longitud']:
            queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE  length({c})<> {l}".format(c=column,l=rule['opc']['longitud'],t=self.tableDummy)
            applied = self.queryApplied(queryMetadata,column)
            if change:
                self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), rpad(col("{c}".format(c=column)),rule['opc']['longitud'],rule['opc']['caracter']) )
                self.dfPyspark.createOrReplaceTempView(self.tableDummy)
                return applied
            else:
                return applied
        else:
            print("no se puede realizar funcion cadena contiene mayor logitud")
            return {"nombre":column,"aplicados":0}

    def ruleGeneralClean( self,rule, change):
      if change:
        query = 'SELECT '
        for column in self.dfPyspark.columns:
          query += 'regexp_replace(trim('+column+'), "( +)"," ") as '+column+', '
        query=query[:-2]+ ' from '+self.tableDummy
        self.dfPyspark = self.sqlCtx.sql(query)
        return {"nombre":"todos los campos","aplicados":"todos los registros"}
      else:
        return {"nombre":"x","aplicados":"y"}

    def ruleTrim(self, column, rule, change):
      tabla= self.tableDummy
      dt = 'string'
      res ,applied = self.validateApplyChanges(dt,tabla,column)
      if not res:
        change=res
      if change:
        if rule['id_rule']=='TrimRule':#trim
          queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE   {c} rlike '  +' ".format(c=column,t=tabla)
          applied = self.queryApplied( queryMetadata,column)
          self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "(  +)", " "))
          self.dfPyspark.createOrReplaceTempView(self.tableDummy)
          return applied
        if rule['id_rule']=='LtrimRule':#ltrim
          queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE  {c} rlike '^ ' ".format(c=column,t=tabla)
          applied = self.queryApplied( queryMetadata,column)
          self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "(^ +)", ""))
          self.dfPyspark.createOrReplaceTempView(self.tableDummy)
          return applied
        if rule['id_rule']=='RtrimRule':#rtrim
          queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE  {c} rlike ' $' ".format(c=column,t=tabla)
          applied = self.queryApplied( queryMetadata,column)
          self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "( +$)", ""))
          self.dfPyspark.createOrReplaceTempView(self.tableDummy)
          return applied
      else:
        return applied

    def ruleLower( self,column , rule,  change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE {c} rlike '[A-Z]'".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), lower(col("{c}".format(c=column))) )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleUpper( self,column, rule, change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE {c} rlike '[a-z]'".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), upper(col("{c}".format(c=column))) )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleInitCap( self,column, rule, change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} ".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), initcap(col("{c}".format(c=column))) )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleLength( self,column, rule, change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t}".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}_length".format(c=column), length(col("{c}".format(c=column))))
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleDecimal( self,column , rule, change):
      tabla= self.tableDummy
      pe=38
      dt = "decimal({pe},{p})".format(pe=pe, p= rule['opc']['precision'])
      res ,applied = self.validateApplyChanges(dt,tabla,column)
      if not res:
        change=res
      queryMetadata = "SELECT count({c}) as {c} FROM {t} where isnull(cast({c} as decimal ({pe},{p}) ))=false".format(c=column,t=self.tableDummy, pe=pe, p= rule['opc']['precision'])
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), col("{c}".format(c=column)).cast(DecimalType(pe,rule['opc']['precision']) ))
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleInteger( self,column, rule, change):
      tabla= self.tableDummy
      dt = "int"
      res ,applied = self.validateApplyChanges(dt,tabla,column)
      if not res:
        change=res
      queryMetadata = "SELECT count({c}) as {c} FROM {t} where isnull(cast({c} as integer ))=false".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), col("{c}".format(c=column)).cast(IntegerType() ))
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleSubMatch( self,column, rule, change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE {c} rLIKE '{b}'".format(c=column,t=self.tableDummy,b=rule['opc']['busqueda'])
      query_posision_match = "SELECT count({c}) as {c} FROM {t} WHERE {c} rLIKE '{b}'".format(c=column,t=self.tableDummy,b=rule['opc']['busqueda'])
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}_subMatch".format(c=column), expr("case when {c} rlike '{b}' then substring( {c},instr({c},{b}) ,length({c})) else 'NoMatch' end".format(c=column,b=rule['opc']['busqueda'])) )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleSub( self,column , rule, change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE length({c}) >= {f}".format(c=column,t=self.tableDummy,f=rule['opc']['fin'])
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}_substring".format(c=column), substring("{c}".format(c=column),rule['opc']['inicio'],rule['opc']['fin'] )   )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleDate2Char( self,column , rule, change):
      tabla= self.tableDummy
      dt = "date"
      res ,applied = self.validateApplyChanges(dt,tabla,column)
      if not res:
        change=res
      queryMetadata = "SELECT count({c}) as {c} FROM {t}".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), date_format(to_date(col("{c}".format(c=column)), rule['opc']['formato_entrada']), rule['opc']['formato_salida']  ) )
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleParserName( self,column,rule,change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t}".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        tmp_sp_df = self.dfPyspark.withColumn("result", expr("udf_parse_name({c})".format(c=column)))\
                        .withColumn("primer_nombre", split(col("result"),',')[0] )\
                        .withColumn("segundo_nombre", split(col("result"),',')[1] )\
                        .withColumn("appelido_paterno", split(col("result"),',')[2] )\
                        .withColumn("appelido_materno", split(col("result"),',')[3] )
        self.dfPyspark = tmp_sp_df.drop("result")
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleDate( self,column,rule,change):
      tabla= self.tableDummy
      dt = "date"
      res ,applied = self.validateApplyChanges(dt,tabla,column)
      if not res:
        change=res
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE udf_is_date({c})='true'".format(c=column,t=self.tableDummy)
      applied = self.queryApplied( queryMetadata,column)
      if change:
        query = 'SELECT '
        query += ''.join( c+', ' if c!=column else 'udf_cadena_to_date2('+c+', "'+rule['opc']['formato_salida']+'") as '+c+', '  for c in self.dfPyspark.columns)
        query=query[:-2]+ ' from '+ self.tableDummy
        self.dfPyspark = self.sqlCtx.sql(query)
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleListCaracter(self, column,rule, opc_bus, remplazo,change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE trim({c}) LIKE '%\{b}%'".format(c=column,t=self.tableDummy,b=opc_bus)
      applied = self.queryApplied( queryMetadata,column,opc_bus)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "\{b}".format(b=opc_bus), "{r}".format(r=remplazo)))
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied

    def ruleListAbrev(self, column,rule, opc_bus, remplazo,change):
      queryMetadata = "SELECT count({c}) as {c} FROM {t} WHERE ( {c} rLIKE '^{b}$' or {c} rLIKE '^{b} ' or {c} rLIKE ' {b} ' or  {c} rLIKE ' {b}$')".format(c=column,t=self.tableDummy,b=opc_bus)
      applied = self.queryApplied( queryMetadata,column,opc_bus)
      if change:
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "^{b}$".format(b=opc_bus), "{rem} ".format(rem=remplazo)))
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), "^{b} ".format(b=opc_bus), "{rem} ".format(rem=remplazo)))
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), " {b} ".format(b=opc_bus), " {rem} ".format(rem=remplazo)))
        self.dfPyspark = self.dfPyspark.withColumn("{c}".format(c=column), regexp_replace(col("{c}".format(c=column)), " {b}$".format(b=opc_bus), " {rem}".format(rem=remplazo)))
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)
        return applied
      else:
        return applied
    def adjFechaProceso(self  ,par ):
        query = 'SELECT '
        query += ''.join(''+column+' as '+column+', ' for column in self.dfPyspark.columns)
        query=query[:-2]+ ', udf_fecha_proceso() as fh_proceso from '+ self.tableDummy
        self.dfPyspark = self.sqlCtx.sql(query)
        self.dfPyspark.createOrReplaceTempView(self.tableDummy)

    ######################################################################## RULES
    ######################################################################## RULES

    def applyRuleByColumn (self,column, rule, change):
        #print("applyRuleByColumn ",rule['id_rule'], type(rule['id_rule']))
        tabla = self.tableDummy
        idRule = rule['id_rule']
        if rule['long']>0:
            rule['opc']= {"longitud": rule['long'], "caracter": rule['output_value']}
        elif rule['input_value']!='' or rule['output_value']!='':
            rule['opc']= {"formato_entrada": rule['input_value'], "formato_salida": rule['output_value']}
        elif rule['precision']>0:
            rule['opc']= {"precision": rule['precision']}
        elif rule['search_value']!='' and rule['id_rule']not in ('ReplaceWordRule','ReplaceCaracterRule'):
            rule['opc']= {"busqueda": rule['search_value']}
        elif idRule=='ReplaceCaracterRule':
            rule['opc']= [{"busqueda": rule['search_value'].split(',') , "remplazo":rule['replace_value']}]
        elif idRule=='ReplaceWordRule':
            rule['opc']= []
            lisSearchValue=rule['search_value'].split(',')
            lisReplaceValue=rule['replace_value'].split(',')
            if len(lisSearchValue)==len(lisReplaceValue):
                for idx, ele in enumerate(lisSearchValue):
                    rule['opc'].append({"busqueda":ele,"remplazo":lisReplaceValue[idx]})
        elif rule['search_value']!='' and rule['replace_value']!='' and rule['id_rule']!='ReplaceCaracterRule':
            rule['opc']= {"busqueda": rule['search_value'] , "remplazo":rule['replace_value']}
        elif rule['inicio']>0:
            rule['opc']= {"inicio": rule['inicio'] , "fin":rule['fin']}
        else:
            rule['opc']= None
        optionsRule = rule['opc']
        if idRule =='ReplaceCaracterRule' and optionsRule:      #regla reemplazos
            if isinstance(optionsRule[0]['busqueda'],list):# lista caracteres
                lisApplyTemp=[]
                for opc_bus in optionsRule[0]['busqueda']:
                    applied =self.ruleListCaracter(column,rule,opc_bus,optionsRule[0]['remplazo'],change)
                    lisApplyTemp.append(applied)
                return lisApplyTemp
        elif idRule =='ReplaceWordRule' and optionsRule:
            if isinstance(optionsRule,list):    # abrevviaciones
                lisApplyTemp=[]
                for opc_bus in optionsRule:
                    applied =self.ruleListAbrev(column,rule,opc_bus['busqueda'], opc_bus['remplazo'],change)
                    lisApplyTemp.append(applied)
                return lisApplyTemp
        elif idRule=='LpadRule':    # regla L_PAD LpadRule
            applied = self.ruleLpad(column,rule,  change)
            return applied
        elif idRule=='RpadRule':    # regla R_PAD
            applied = self.ruleRpad(column,rule,  change)
            return applied
        elif (idRule=='TrimRule' or idRule=='LtrimRule' or idRule=='RtrimRule'):    #regla trim
            applied = self.ruleTrim(column,rule, change)
            return  applied
        elif idRule=='LowerRule':    # regla minusculas
            applied = self.ruleLower(column,rule,  change)
            return applied
        elif idRule=='UpperRule':    #regla  mayusculas
            applied = self.ruleUpper(column,rule,  change)
            return applied
        elif idRule=='LengthRule':    #regla lenght
            applied = self.ruleLength(column,rule,  change)
            return applied
        elif idRule=='DateFormatRule':    # date_to_char cambia el formato de fecha
            applied = self.ruleDate2Char(column,rule,  change)
            return applied
        elif idRule=='InitCapRule':    # una cadena contendra la primera letra mayuscula y el resto minusculas
            applied = self.ruleInitCap(column,rule,  change)
            return applied
        elif idRule=='FormatDecimalRule':    # cadena a decimal
            applied = self.ruleDecimal(column,rule,  change)
            return applied
        elif idRule=='ToIntegerRule':    # cadena a entero
            applied = self.ruleInteger(column,rule,  change)
            return applied
        elif idRule=='SubstringMatchRule':    # substring ocuurence
            applied = self.ruleSubMatch(column,rule,  change)
            return applied
        elif idRule=='SubstringRule':    # substring
            applied = self.ruleSub(column,rule,  change)
            return applied
        elif idRule=='ParserNamedRule':    # substring
            applied = self.ruleParserName(column,rule,  change)
            return applied
        elif idRule=='ToDateRule':    # cadena a fecha
            return self.ruleDate(column,rule,change)
        elif idRule=='CleanAllRule':
            return self.ruleGeneralClean(rule,change)

    def getMetadataRule(lisFieldsChange, metaDataRegister):
        liscolumns =[]
        lisChanges=[]
        for field in lisFieldsChange:
            if field:
                if isinstance(field,list):
                    lisOption=[]
                    nameColumn=''
                    for dic in field:
                        if 'busqueda' in dic:
                            lisOption.append({'busqueda':dic['busqueda'],'aplicados':dic['aplicados']})
                            nameColumn=dic['nombre']
                    liscolumns.append(nameColumn)
                    lisChanges.append(lisOption)
                else:
                    liscolumns.append(field['nombre'])
                    lisChanges.append(field['aplicados'])
        metaDataRegister['columnas']=liscolumns
        metaDataRegister['cambios']=lisChanges
        return metaDataRegister

    def menuRules(self ,pars_ ):
        self.reglas=[]
        for idx , rule in enumerate(sorted(pars_['rules'], key=lambda k: k['orden'])):
            queryTotal = "SELECT count(*) as conteo_registro FROM {table} ".format(table=self.tableDummy)
            total  = self.sqlCtx.sql(queryTotal).collect()[0][0]
            metadataRule = CleaningFile.catchApplyRule(rule, total)
            listChangeFields = []
            # aplica la regla a la columna _indicada
            for column in rule['columns']:
                dictChanges = self.applyRuleByColumn(column,rule , change=True)
                listChangeFields.append(dictChanges)
            self.reglas.append(CleaningFile.getMetadataRule(listChangeFields,metadataRule ))
        self.adjFechaProceso( pars_  )

    def helpCreateHeader(self,header):
        listHeader=[]
        if self.haveHeaders:
          listHeader=header.split(self.sep)
        else:
          for idx,elem in enumerate(header.split(self.sep)):
              listHeader.append("column_" + str ( idx+1 ) )
        return listHeader

    def helpGetBadLines(self ):
      if len(self.badDfPyspark.take(1))>0:
        self.lisBadLines= [(row._2) for row in self.badDfPyspark.select('_2').collect()]
      else:
        self.lisBadLines= 0

    def exportFileResult (self, pars_):
        parTgt = pars_['path_tgt']
        parNom = pars_['name']
        pathTemp = parTgt
        tgt = pathTemp + parNom
        if self.ds_conexion!='local':
            if not os.path.exists(pathTemp):
                os.makedirs(parTgt)
            self.dfPyspark.repartition(1).write.csv( path=tgt,             mode="overwrite", header=self.haveHeaders, sep=self.sep)
        else:
            if not os.path.exists(pathTemp):
                os.makedirs(pathTemp)
            self.dfPyspark.repartition(1).write.csv( path=parTgt+parNom, mode="overwrite", header=self.haveHeaders, sep=self.sep)

    def initProcess(self):
        self.initialDateTime=timezone.now()
        pars={}
        rules=[]
        pars["path_src"]= '/'.join(self.filename.split('/')[0:-1])
        pars["path_tgt"]= self.destinationFileName
        pars['name'] = Path(self.filename).parts[-1]
        pars['header'] = self.haveHeaders
        pars['delimiter'] = self.sep
        self.tableDummy = 'TABLA'


        for rule in CleaningFileOrderedRulesInColumns.objects.filter(cleaningFile = self):
            ruleDict={'orden':rule.order,'id_rule':'','long':0,'replace_value':'','input_value':'','output_value':'','precision':0,'search_value':'','replace_value':'','inicio':0,'fin':0}


            for r in rule.rules.all():
                regla = CleaningFileRule.objects.get(id=r.pk)
                if regla.content_type.model_class()().getClassName()=='LpadRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['long']=LpadRule.objects.get(id=regla.object_id).length
                    ruleDict['output_value']=LpadRule.objects.get(id=regla.object_id).caracter
                elif regla.content_type.model_class()().getClassName()=='TrimRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='LtrimRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='RtrimRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='UpperRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='LowerRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='InitCapRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='LengthRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='ParserNamedRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='CleanAllRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='ToIntegerRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                elif regla.content_type.model_class()().getClassName()=='SubstringMatchRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['search_value']=SubstringMatchRule.objects.get(id=regla.object_id).patron
                elif regla.content_type.model_class()().getClassName()=='SubstringRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['inicio']=SubstringRule.objects.get(id=regla.object_id).init
                    ruleDict['fin']=SubstringRule.objects.get(id=regla.object_id).end
                elif regla.content_type.model_class()().getClassName()=='FormatDecimalRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['precision']=FormatDecimalRule.objects.get(id=regla.object_id).decimal
                elif regla.content_type.model_class()().getClassName()=='RpadRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['long']=RpadRule.objects.get(id=regla.object_id).length
                    ruleDict['output_value']=RpadRule.objects.get(id=regla.object_id).caracter
                elif regla.content_type.model_class()().getClassName()=='ReplaceCaracterRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['search_value']=ReplaceCaracterRule.objects.get(id=regla.object_id).search
                    ruleDict['replace_value']=ReplaceCaracterRule.objects.get(id=regla.object_id).replace
                elif regla.content_type.model_class()().getClassName()=='ReplaceWordRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['search_value']=ReplaceWordRule.objects.get(id=regla.object_id).search
                    ruleDict['replace_value']=ReplaceWordRule.objects.get(id=regla.object_id).replace
                elif regla.content_type.model_class()().getClassName()=='DateFormatRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['input_value']=DateFormatRule.objects.get(id=regla.object_id).inputFormat
                    ruleDict['output_value']=DateFormatRule.objects.get(id=regla.object_id).outputFormat
                elif regla.content_type.model_class()().getClassName()=='ToDateRule':
                    ruleDict['id_rule']=regla.content_type.model_class()().getClassName()
                    ruleDict['output_value']=ToDateRule.objects.get(id=regla.object_id).outputFormat

            col=[]
            for c in rule.columns.all():
                columna = CleaningFileColumn.objects.get(id=c.pk)
                col.append(columna.name)
            ruleDict['columns']=col
            rules.append(ruleDict)

        pars['rules'] = rules
        if os.path.isfile(self.filename):
            self.conf = pyspark.SparkConf().setAppName("trn_arc_pyspark_"+str(pars['name'])).setMaster("local[*]")
            self.sc = pyspark.SparkContext.getOrCreate(conf=self.conf)
            self.sqlCtx = SQLContext(self.sc)
            self.sc.addPyFile("/app/quda/clng/udf.py")
            self.sqlCtx.udf.register('udf_cadena_to_date2', cadena_to_date2)
            self.sqlCtx.udf.register('udf_parse_name', parse_name)
            self.sqlCtx.udf.register('udf_is_date', is_date)
            self.sqlCtx.udf.register('udf_fecha_proceso', fecha_proceso)
            print("init",self.sc)
            pathTempCopy =self.filename
            LocalFile = self.sc.textFile(pathTempCopy)
            headerFile = LocalFile.first()
            if self.haveHeaders:
              lisHead = headerFile.split(self.sep)
            else:
              pars['lisHeader'] = self.helpCreateHeader(headerFile)
              lisHead = pars['lisHeader']
            parserLines = LocalFile.map(lambda linea: linea.split(pars['delimiter'])).filter(lambda l :not str(l).startswith(headerFile)).filter(lambda linea :len(linea) ==len(lisHead))
            badParserLines = LocalFile.map(lambda linea: linea.split(pars['delimiter'])).zipWithIndex().filter(lambda linea :len(linea[0]) !=len(lisHead))
            # realiza el parseo de lineas
            if len(badParserLines.take(1)) > 0 :
              self.badDfPyspark = badParserLines.toDF()
            else:
              schema = StructType([StructField("FIELDNAME_1",StringType(), True),StructField("FIELDNAME_2", StringType(), True)])
              self.badDfPyspark = self.sqlCtx.createDataFrame(self.sc.emptyRDD(), schema)
            self.dfPyspark = parserLines.toDF(lisHead)
            self.helpGetBadLines()
            self.numBadLines=badParserLines.count()
            self.numTotalLines=LocalFile.count()
            # inicializa la tabla de pyspark sql
            self.dfPyspark.createOrReplaceTempView(self.tableDummy)
            self.menuRules( pars)
            self.exportFileResult ( pars)
            self.resultRules = self.log_dict()
            self.finalDateTime=timezone.now()
            self.save()
            self.sc.stop()
            print(self.log_dict())
            return {"mensaje":"archivo procesado exitosamente {var}". format(var =self.filename)}
        else:
            dictResult ={"mensaje":"archivo no pudo ser proceseado :{var}". format(var =self.filename),
                         "Error": "Check archivo este en path correcto"}
            print(dictResult)
            self.resultRules = dictResult
            self.finalDateTime=timezone.now()
            self.save()
            return dictResult

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

