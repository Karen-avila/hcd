import sys, os, json, glob, re

from datetime import datetime
from hdfs3    import HDFileSystem


def now():
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#regresa una conexion a hadoop , se tiene que cambiar al metadato de mongo
def trn_arc_ayu_conexion_hdfs():
  try:
    conf={'hadoop.security.authentication': 'kerberos','hadoop.rpc.protection':'authenticate'}
    ticket_path_keytab='/home/centos/Documents/KeyTab/usrjaga1.keytab'
    ticket_path_cache='FILE:/tmp/krb5cc_1000'  
    hdfs=HDFileSystem(host='10.100.6.82' ,port=8020 ,principal='jaga1@IMMS.GOB.MX' ,driver='libhdfs' ,pars=conf ,ticket_cache=ticket_path_cache      )
  except Exception as e:
    #sys.stderr.write("common::main() : [ERROR]: output = %s" % (e))
    print("Se trabajara de forma local")
    hdfs=None

  return hdfs


def exepcion_archivo_local(logproc):
  logproc.fh_fin_copia = now()
  logproc.ds_copia_estatus = 'No es necesaria la Copia temporal, ya se trabaja local'
  logproc.ds_conexion      = 'local'
  return logproc



#valida si el archivo existe en hadoop y realiza una copia en una ruta temporal local
def trn_arc_ayu_crea_directorio_src(hdfs, parametros, logproc ):
  logproc.fh_ini_copia = now()
  src = parametros['archivo']['ruta_src']
  nom = parametros['archivo']['nombre']
  ruta_copia     = 'tmp'+ src
  ruta_tmp_copia = ruta_copia + nom
  if hdfs:
    if hdfs.isfile(src + nom):
      if not os.path.exists(ruta_copia):
        os.makedirs(ruta_copia)    
      hdfs.get( src + nom, ruta_tmp_copia)        
      logproc.ds_copia_estatus='Copia temporal local lista'
      logproc.fh_fin_copia    = now()
      logproc.ds_conexion     ='servidor remoto'      
      return logproc , ruta_tmp_copia
    elif os.path.isfile(parametros['archivo']['ruta_src']+parametros['archivo']['nombre']):
      logproc = exepcion_archivo_local(logproc)
      return logproc, src+nom
    else:
      logproc.fh_fin_copia= now()
      logproc.ds_copia_estatus='Error archivo {} no existe en hdfs'.format(src + nom)
      return logproc, False
  else:      
    if os.path.isfile(parametros['archivo']['ruta_src']+parametros['archivo']['nombre']):
      logproc = exepcion_archivo_local(logproc)      
      return logproc, src+nom
      
#genera un encabezado generico para archivos sin que no tienen encabezado
def trn_arc_ayu_gen_encabezado(encabezado, parametros ):
  lista_encabezado=[]
  for idx,elem in enumerate(encabezado.split(parametros['separador'])):
    lista_encabezado.append("column_" + str ( idx+1 ) )
  return lista_encabezado



def busca_archivo_y_renombra(target, nom):
  renombrado_archivo =''
  lista_archivos = glob.glob(target+'/*')    
  #recorre la lista de archivos creados en el export para renombrarlo a su nombre original
  for arc in lista_archivos:
    #if re.search( "^tmp.*\.csv$", arc):
    if re.search( "\.csv$", arc):
      renombrado_archivo = arc      
  os.rename(renombrado_archivo,target+'/'+nom )
  return True, None

#realiza un renombrado de archivos ya que pyspark al hacer el export agrega n ccaracteres al nombre del archivo resultado
def trn_arc_ayu_rnm_archivos(parametros,logproc):
  ruta_tgt = parametros['archivo']['ruta_tgt']
  nombre   = parametros['archivo']['nombre']
  tgt                ='tmp'+ruta_tgt+nombre  
  if logproc.ds_conexion!='local': 
    try:
      #dir_ruta       = os.path.dirname(os.path.realpath(__file__))
      bandera, error =  busca_archivo_y_renombra(tgt, nombre)      
      return bandera, error
    except Exception as e:
      print("Error en el renombrado de archivo pyspark remoto: {var}".format(var=str(e)))
      return False, str(e)
  else:
    try:    
      bandera, error =  busca_archivo_y_renombra(ruta_tgt+nombre, nombre)            
      return bandera, error
    except Exception as e:          
      print("Error en el renombrado de archivo pyspark local: {var}".format(var=str(e)))
      return False, str(e)


def trn_arc_ayu_sube_lt ( parametros, logproc, hdfs):
  logproc.fh_ini_sube_lt=now()
  bandera , error = trn_arc_ayu_rnm_archivos(parametros, logproc)
  if logproc.ds_conexion!='local':
    if bandera: 

      hdfs.put('tmp'+parametros['archivo']['ruta_tgt']+parametros['archivo']['nombre']+'/'+parametros['archivo']['nombre'], parametros['archivo']['ruta_tgt']+parametros['archivo']['nombre'])
      logproc.evidencia_lt      = hdfs.ls( parametros['archivo']['ruta_tgt'])
      logproc.evidencia_lt_info = hdfs.info( parametros['archivo']['ruta_tgt']+parametros['archivo']['nombre'])
      logproc.ds_export_estatus = "Proceso finaliza archivo fue subido a lt remoto."
  else:
    logproc.ds_export_estatus = "Proceso no realizado , se realizo transformacion local"
  logproc.fh_fin_sube_lt=now()
  return logproc

#realiza la exportacion del dataframe una vez que ya se han realizado las transformaciones indicadas
def trn_arc_ayu_arc_exporta (sp_df, parametros, logproc):
  logproc.fh_ini_export = now()
  #si el archivo es nuevo genera un espejo en la ruta temp para dejar el archivo de manera local y luego hacer la subida al servidor lt  
  par_tgt = parametros['archivo']['ruta_tgt']
  par_nom = parametros['archivo']['nombre']
  if logproc.ds_conexion!='local':
    ruta_temp = 'tmp'     + par_tgt
    tgt       = ruta_temp + par_nom
    if not os.path.exists(ruta_temp):
      os.makedirs(par_tgt)
    sp_df.repartition(1).write.csv( path=tgt,             mode="overwrite", header="false", sep=parametros['separador'])
  else:
    if not os.path.exists(par_tgt):
      os.makedirs(par_tgt)
    sp_df.repartition(1).write.csv( path=par_tgt+par_nom, mode="overwrite", header="false", sep=parametros['separador'])
  logproc.fh_fin_export = now()
  return logproc  

#obtiene la lista de lineas de malas lineas
def trn_arc_ayu_mal_lineas(sp_df, logproc):
  li_lin_malas = sp_df.select('_2').collect()
  logproc.li_lin_malas = li_lin_malas[0]
  return logproc