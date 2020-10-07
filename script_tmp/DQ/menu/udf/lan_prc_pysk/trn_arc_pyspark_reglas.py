import sys, os, json, glob, re

from   trn_arc_pyspark_ayuda  import now






  # registra 2 funciones udf al contexto sql
#  sqlCtx.udf.register('udf_cadena_to_date', cadena_to_date)

#genera el query dinamico y ejecuta el query en pyspark sql ------- quita espacios
def regla_trim( sp_df , lis_encabezado , tabla , sqlCtx):
  str_query_trim = 'SELECT '
  str_query_trim += ''.join('trim('+columna+') as '+columna+', ' for columna in lis_encabezado) 
  #elimina la ultima coma adjunta en for 
  str_query_trim=str_query_trim[:-2]+ ' from '+ tabla
  sp_df = sqlCtx.sql(str_query_trim)    
  sp_df.createOrReplaceTempView(tabla)
  
  return sp_df


#genera el query dinamico y ejecuta el query en pyspark sql ------- minusculas
def regla_lower( sp_df , lis_encabezado , tabla , sqlCtx):
  str_query_lower = 'SELECT '
  str_query_lower += ''.join('lower('+columna+') as '+columna+', ' for columna in lis_encabezado) 
  #elimina la ultima coma adjunta en for 
  str_query_lower=str_query_lower[:-2]+ ' from '+ tabla
  sp_df = sqlCtx.sql(str_query_lower)
  sp_df.createOrReplaceTempView(tabla)

  return sp_df

#genera el query dinamico y ejecuta el query en pyspark sql ------- fechas
def regla_date( sp_df , lis_encabezado , tabla , sqlCtx):
  str_query_date = 'SELECT '
  str_query_date += ''.join('udf_cadena_to_date('+columna+') as '+columna+', ' for columna in lis_encabezado) 
  #elimina la ultima coma adjunta en for 
  str_query_date=str_query_date[:-2]+ ' from '+ tabla
  sp_df = sqlCtx.sql(str_query_date)
  sp_df.createOrReplaceTempView(tabla)

  return sp_df






def adj_col_fh_proceso(sp_df , lis_encabezado , tabla , sqlCtx):
  str_query = 'SELECT '
  str_query += ''.join(''+columna+' as '+columna+', ' for columna in lis_encabezado) 
  #elimina la ultima coma adjunta en for 
  str_query=str_query[:-2]+ ', udf_fecha_proceso() as fh_proceso from '+ tabla
  sp_df = sqlCtx.sql(str_query)
  sp_df.createOrReplaceTempView(tabla)

  return sp_df






#menu de reglas
def trn_arc_menu_reglas( parametros,dataframe_pyspark, lista_encabezado, logproc , tabla, sqlCtx):  
  resultado=''
  for indice , regla in enumerate(parametros['reglas']):
    # llama a la regla TRIM 
    if regla['id_funcion'] == 17:
      dataframe_pyspark = regla_trim(dataframe_pyspark, lista_encabezado , tabla , sqlCtx )
    #lama a la regla lower
    if regla['id_funcion'] == 2:
      dataframe_pyspark = regla_lower(dataframe_pyspark, lista_encabezado , tabla , sqlCtx )
    #lama a la regla fecha
    if regla['id_funcion'] == 12:
      #dataframe_pyspark = regla_date(dataframe_pyspark, lista_encabezado , tabla , sqlCtx )
      pass
  dataframe_pyspark = adj_col_fh_proceso(dataframe_pyspark, lista_encabezado , tabla , sqlCtx )
    
  logproc.fh_fin_proceso=now()
  return logproc, dataframe_pyspark
