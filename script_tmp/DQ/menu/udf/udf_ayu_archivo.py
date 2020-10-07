
import os,sys,ast
from menu.obj.obj_clases         import Archivo
from menu.cfg.cfg_reglas         import reglas
from menu.cfg.cfg_conexion       import hdfs
import glob
from os import listdir
from os.path import isfile, join
#agrega los parametros de archivo a la instancia de resultado
def udf_ayu_agr_obj_archivos(resultado):
    lis_obj_archivo=[]
    lis_temp=[]

    for idx, archivo in enumerate(resultado.archivos):                        
        if str(archivo.nombre) == str(resultado.opc_asterico): 
            print("miguel",str(archivo.nombre) , str(resultado.opc_asterico))

            #opcion asterisco todos los archivos 
            try:
                lis_temp=[f for f in  hdfs.ls(resultado.ruta_src) if hdfs.isfile(join(resultado.ruta_src, f))]
            except Exception as e:
                lis_temp=[f for f in os.listdir(resultado.ruta_src) if os.path.isfile(join(resultado.ruta_src, f))]                
            for idy,a in enumerate(lis_temp):
                lis_obj_archivo.append(Archivo(id_archivo=idy, nombre=a, separador=resultado.separador, encabezado=resultado.encabezado ))
        elif isinstance(archivo, Archivo):
            lis_obj_archivo.append(Archivo(id_archivo=idx, nombre=archivo.nombre, separador=archivo.separador, encabezado=archivo.encabezado    ))            
        else :            
            lis_obj_archivo.append(Archivo(id_archivo=idx, nombre=archivo, separador=resultado.separador, encabezado=resultado.encabezado ))
    resultado.archivos = lis_obj_archivo
    return resultado

#pasa valores unicode a str recursivamente en diccionarios y listas de diccionarios
def convert(input):
    if isinstance(input, dict):
        return dict((convert(key), convert(value)) for key, value in input.iteritems())
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

#agrega a resultados las reglas
def udf_ayu_agr_reglas(resultado):
    try:
        re=[]
        for ele in reglas:
            n_ele=convert(ele)        
            re.append(n_ele)
        resultado.reglas= re
        return resultado
    except Exception as  e:
        resultado.reglas= reglas
        return resultado



def udf_ayu_val_ori_datos(menu,resultado):    
    flag = False
    if hdfs:        
        if not menu:
            if hdfs.isdir(resultado.ruta_src):
                flag=True
        elif hdfs.isdir(menu.ruta_src):
            flag=True
        elif os.path.isdir(menu.ruta_src):
            print("hay conexion la ruta es local: {v}".format(v=hdfs),resultado.ruta_src,menu.ruta_src)
            flag=True
    else:
        print("Sin conexion a servidor hdfs: {v}".format(v=hdfs),resultado.ruta_src,menu.ruta_src)
        if not menu:
            if os.path.isdir(resultado.ruta_src):
                flag=True
        elif os.path.isdir(menu.ruta_src):
            flag=True    
    return flag


def udf_ayu_val_exi_archivo(archivo):
    
    flag = False
    if hdfs:        
        if hdfs.isfile(archivo.ruta_src+archivo.nombre):            
            flag =True
        elif os.path.isfile(archivo.ruta_src+archivo.nombre):
            flag = True
    else:
        print(archivo.ruta_src+archivo.nombre)

        if os.path.isfile(archivo.ruta_src+archivo.nombre):        
            flag =True
    return flag

