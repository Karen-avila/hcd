
import sys
import os, json
import glob
import re

from datetime import datetime
import pyspark
from   pyspark.sql.types      import *
from   pyspark.sql.functions  import lower, col , current_date,unix_timestamp,to_date,lit
from   pyspark.sql            import SQLContext
from   hdfs3                  import HDFileSystem
from pyspark.sql            import SQLContext,SparkSession
from   obj.obj_pys_clases     import LogProcesos
from   cfg.cfg_par_pyspark    import cfg_obt_par_pyspark
from   trn_arc_pyspark_ayuda  import now,trn_arc_ayu_conexion_hdfs,trn_arc_ayu_crea_directorio_src,trn_arc_ayu_gen_encabezado,trn_arc_ayu_sube_lt 
from   trn_arc_pyspark_ayuda  import trn_arc_ayu_mal_lineas,trn_arc_ayu_arc_exporta
from   trn_arc_pyspark_udf    import cadena_to_date, fecha_proceso

from   trn_arc_pyspark_reglas import trn_arc_menu_reglas


from dateutil.parser import parse
#from pyspark.sql import SparkSession


# recibe el argumento que contiene el json con los parametros que trabajara el transformador --spark-submit
args =sys.argv[1:]
parametros = cfg_obt_par_pyspark(args[0])
hdfs       = trn_arc_ayu_conexion_hdfs()


print(type(parametros))
parametros = json.loads(parametros)
print(type(parametros))
print(parametros)

ruta_src         = parametros['archivo']['ruta_src']
ruta_tgt         = parametros['archivo']['ruta_tgt']
nom_src          = parametros['archivo']['nombre']
archivo_src      = ruta_src + nom_src
tabla            = 'DF_TABLA'

# genera los settings para trabajar con pyspark
spark = SparkSession.builder.master('spark://172.29.0.224:7070').appName("trans_archivo_pyspark_General").getOrCreate();
sc               = spark.sparkContext
sc.addPyFile("menu/udf/lan_prc_pysk/trn_arc_pyspark_reglas.py")
sc.addPyFile("menu/udf/lan_prc_pysk/trn_arc_pyspark_udf.py")


sqlCtx = SQLContext(sc)
sqlCtx.udf.register('udf_cadena_to_date', cadena_to_date)
sqlCtx.udf.register('udf_fecha_proceso', fecha_proceso)

sc.setLogLevel('WARN')
sc.setLogLevel('ERROR')

#inicia instancia de la metadata del proceso
logprocesos = LogProcesos(id=0, nombre=nom_src, ruta_src=ruta_src, ruta_tgt=ruta_tgt)
#valida si el archivo existe en hadoop y realiza una copia en una ruta temporal local
logprocesos, ruta_tmp_copia  = trn_arc_ayu_crea_directorio_src(hdfs,parametros, logprocesos)



#lee el archivo de forma local
#try:
logprocesos.fh_ini_proceso = now()

archivo_plano_local        = sc.textFile(ruta_tmp_copia)
encabezado                 = archivo_plano_local.first()
#genera un encabezado generico para archivos sin que no tienen encabezado
lista_encabezado  = trn_arc_ayu_gen_encabezado(encabezado,parametros)
# realiza el parseo de lineas
parseo_lineas     = archivo_plano_local.map(lambda linea: linea.split(parametros['separador'])).filter(lambda linea :len(linea) ==len(lista_encabezado))
#malas lineas 
mal_parseo_lineas = archivo_plano_local.map(lambda linea: linea.split(parametros['separador'])).zipWithIndex().filter(lambda linea :len(linea[0]) !=len(lista_encabezado))


dataframe_pyspark = parseo_lineas.toDF(lista_encabezado)
malas_lineas      = mal_parseo_lineas.toDF()

logprocesos       = trn_arc_ayu_mal_lineas(malas_lineas, logprocesos)

# crea vista para trabajar con pyspark -sql
#malas_lineas.show()
logprocesos.nu_lin_malas=malas_lineas.count()
# inicializa la tabla de pyspark sql
dataframe_pyspark.createOrReplaceTempView(tabla)
#aplica reglas
logprocesos, dataframe_pyspark_2 = trn_arc_menu_reglas( parametros, dataframe_pyspark, lista_encabezado, logprocesos, tabla, sqlCtx)
#realiza el export del dataframe pyspark a csv
logprocesos = trn_arc_ayu_arc_exporta (dataframe_pyspark_2, parametros, logprocesos)
#sube el archivo csv a servidor remoto
logprocesos = trn_arc_ayu_sube_lt ( parametros, logprocesos,hdfs)

logprocesos.fh_final=now()
json_object = json.dumps(logprocesos.log_dict())
print(">>>>>>>>>>>>>")
print(json_object)
"""

"""