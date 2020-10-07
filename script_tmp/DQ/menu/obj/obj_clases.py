# -*- coding: utf-8 -*-
import os, sys, datetime
from colorama import Style,Fore

class Archivo(object):
    # The class "constructor" - It's actually an initializer
    bandera_existe = False
    ruta_src = ''
    ruta_tgt = ''
    def __init__(self, id_archivo=0, nombre='', separador='', encabezado=False):
        self.id_archivo = id_archivo
        self.nombre = nombre
        self.separador = separador
        self.encabezado = encabezado

    def as_dict(self):
        return {
            'id_archivo': self.id_archivo,
            'ruta_src': str(self.ruta_src),
            'ruta_tgt': str(self.ruta_tgt),
            'nombre': str(self.nombre),
            'separador': self.separador,
            'encabezado': self.encabezado
        }


class Menu(object):
    # The class "constructor" - It's actually an initializer
    
    def __init__(self, id_menu=0, argumentos_menu={}, archivos=[], reglas={}, ruta_src='',ruta_tgt='',separador='',encabezado=False):
        # super(Archivo, self).__init__()
        self.id_menu = id_menu
        self.argumentos_menu = argumentos_menu
        self.archivos = archivos
        self.ruta_src = ruta_src
        self.ruta_tgt = ruta_tgt
        self.separador = separador
        self.encabezado = encabezado
        self.reglas = reglas

    def as_dict(self):
        return {'id_menu': self.id_menu,
                'argumentos_menu': self.argumentos_menu,
                'ruta': self.ruta,
                'archivos': self.archivos
                }


class Proceso(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, id_proceso=0, nombre_archivo='', fh_inicio=datetime.datetime.now(), fh_fin='', ds_estatus=''):
        self.id_proceso = id_proceso
        self.nombre_archivo = nombre_archivo
        self.fh_inicio = fh_inicio
        self.fh_fin = fh_fin
        self.ds_estatus = ds_estatus

    def log_fun_dic(self):
        if int(self.id) != 0:
            print("algo va mal")
        ds_estatus = 'Sin Estatus'
        return {'id': self.id,
                'nombre': self.nombre,
                'fh_inicio': self.fh_inicio,
                'fh_fin': self.fh_fin,
                'ds_estatus': self.ds_estatus,

                }


class LogProcesos(object):
    # The class "constructor" - It's actually an initializer
    def __init__(self, id=0, nombre='', fh_inicio=datetime.datetime.now(), fh_fin='', ds_estatus=''):
        self.id = id
        self.nombre = nombre
        self.fh_inicio = fh_inicio
        self.fh_fin = fh_fin
        self.ds_estatus = ds_estatus

    def log_fun_dic(self):
        if int(self.id) != 0:
            print("algo va mal")
        ds_estatus = 'Sin Estatus'
        return {'id': self.id,
                'nombre': self.nombre,
                'fh_inicio': self.fh_inicio,
                'fh_fin': self.fh_fin,
                'ds_estatus': self.ds_estatus,

                }


class Resultado(object):
    # The class "constructor" - It's actually an initializer
    msj_0           = Style.BRIGHT + "Capture una opción del menú: "
    msj_1           = Style.BRIGHT + 'Seleccione una opción del menú: '
    msj_nom_archivo = Style.BRIGHT + Fore.WHITE + '\nIntroduzca el nombre del archivo(s) a {var} separados por , con su extensión:\n >>> Si son varios escriba * para tomar todos los que estaran en la ruta  '
    msj_ruta_src = Style.BRIGHT + Fore.WHITE + 'Introduzca la ruta donde se encuentra almacenado el archivo : '
    msj_ruta_tgt = Style.BRIGHT + Fore.WHITE + 'Introduzca la ruta de destino para el archivo : '
    msj_opciones_delimitador =Style.BRIGHT + Fore.CYAN + '\nOpciones de delimitadores: \n' + Style.BRIGHT + Fore.YELLOW + '\n0. Coma. \n1. Pipe. \n2. Tab. \n3. Tilde. \n4. Punto y Coma. \n5. Otro.'    
    msj_delimitador = Style.BRIGHT + Fore.WHITE + '\nIndique el delimitador del archivo (0-{var}): '
    msj_opcion_delimitador = Style.BRIGHT + Fore.WHITE + 'Capture el delimitador de el o los archivos: '
    msj_separador    = Style.BRIGHT + Fore.RED + '\n¡Aviso! ', Style.BRIGHT + Fore.WHITE + 'La longitud del separador deberá ser igual a 1, intente de nuevo. '
    msj_separador_2  = Style.BRIGHT + Fore.WHITE + 'El delimitador del archivo indicado por el usuario es: {var}'
    msj_encabezado   = Style.BRIGHT + Fore.WHITE + '¿El archivo tiene encabezados? (S/N):'
    msj_trt_archivo  = Style.BRIGHT + Fore.YELLOW + '\nEspere un momento, se está cargando en la aplicación el contenido del archivo:'
    msj_trt_archivo_no  = Style.BRIGHT + Fore.YELLOW + '\nEl archivo no se encontro en la ruta especificada:'
    #dic_delimitadores  = {'0':',','1':'|','2':'\t','3':'~','4':';', '5':'^'}
    dic_delimitadores  = {'0':',','1':'|','2':'\t','3':'~','4':';'}
    opc_otro_delimitador  = 5
    opc_asterico  = '*'
    ban_exi_ruta     = False
    ban_exi_archivo  = False
    ruta_par_pyspark ='tmp/par/'
    cmd_pyspark      ='spark-submit'
    scp_pyspark      ='menu/udf/lan_prc_pysk/trn_arc_pyspark.py'
    par_pyspark      =''
    ruta_src         =''
    ruta_tgt         =''



    alerta_0 = '¡Aviso! La opción qdddue capturó no es válida. | Pulse la tecla [Enter] para continuar ...'
    alerta_1 =  Style.BRIGHT + Fore.RED + '¡Aviso! La opción que seleccionó no es válida. ' + Style.BRIGHT + Fore.WHITE + 'Pulse la tecla [Enter] para continuar ...'
    def __init__(self, id_resultado=0, argumentos_menu={}, archivos=[], reglas=[],separador='',encabezado=False):
        # super(Archivo, self).__init__()
        self.id_resultado = id_resultado
        self.argumentos_menu = argumentos_menu
        self.archivos = archivos
        self.reglas = reglas
        self.separador = separador
        self.encabezado = encabezado
        

    def as_dict(self):
        return {'id_resultado': self.id_resultado,
                'argumentos_menu': self.argumentos_menu,
                'ban_exi_ruta': self.ban_exi_ruta,
                'ban_exi_archivo': self.ban_exi_archivo,                
                'reglas': self.reglas,
                'separador': self.separador,
                'encabezado': self.encabezado
                }

