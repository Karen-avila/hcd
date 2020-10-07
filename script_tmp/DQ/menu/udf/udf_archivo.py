# -*- coding: utf-8 -*-
import os,sys,io
from os      import listdir
from os.path import isfile, join

from io import open
from menu.udf.udf_ayuda                       import limpia_pantalla
from menu.udf.udf_ayu_archivo                 import udf_ayu_agr_obj_archivos,udf_ayu_agr_reglas, udf_ayu_val_ori_datos,udf_ayu_val_exi_archivo
from menu.udf.lan_prc_pysk.lan_procesos       import lan_prc_pyspark

#from menu.udf.udf_dataFrame      import udf_gen_dataframe

from   colorama import Style, Fore, init
import json





############################################################################################
# Descripción: Función que solicita al usuario seleccionar un delimitador para el          #
#              archivo a analizar.                                                         # 
# Autor: CRDM para Softtek.                                                                #
# Fecha de creación: 16/06/2020.                                                           #
# Parametros de entrada: No aplica.                                                        #
# Retorna:                                                                                 #
#     El delimitador del archivo a analizar seleccionado por el usuario.                   #
# Modificó: No aplica.                                                                     #
# Fecha de última modificación: No aplica.                                                 #
# Descripción de la última modificación: No aplica.                                        #
############################################################################################
def udf_delimitador(menu,resultado):    
    # Se inicializa colorama.
    init(autoreset=True)        
    # Declaracion de la tupla de opciones
    tupla_opciones = ('0','1','2','3','4','5') 
    # Declaracion bandera ciclo while
    while True:
        # Solicita al usuario el delimitador del archivo.
        #v_opcion_menu = str(input(Style.BRIGHT + Fore.WHITE + '\nIndique el delimitador del archivo (0-5): '))
        v_opcion_menu = None
        if not menu:            
            resultado.separador = str(input(resultado.msj_delimitador.format(var=len(resultado.dic_delimitadores) )))
            v_opcion_menu = resultado.separador
        else:
            if not(menu.archivos==resultado.opc_asterico):
                for k,v in resultado.dic_delimitadores.items():                                
                    if menu.archivos[0].separador == v:
                        v_opcion_menu = k
                        break
                if not v_opcion_menu:                
                    v_opcion_menu = resultado.opc_otro_delimitador
                    resultado.separador = str(menu.archivos[0].separador)                        
            else:
                v_opcion_menu = resultado.opc_otro_delimitador
                resultado.separador = str(menu.encabezado)                        

        # Valida que el usuario haya capturado una opción valida.
        if str(v_opcion_menu) in tupla_opciones:
            if v_opcion_menu != '5':
                # Asigna el delimitador seleccionado del menú de opciones.
                if not menu.archivos==resultado.opc_asterico:
                    resultado.separador = menu.archivos[0].separador
                else:    
                    resultado.separador = menu.separador
                pass
            else:
                # Solicita al usuario que capture el delimitador del archivo
                while True:
                    if not menu:
                        resultado.separador = str(input(resultado.msj_opcion_delimitador)).strip()
                    else:
                        resultado.separador = str(menu.opcion_delimitador).strip()
                    if len(resultado.separador) == 1:
                        break
                    else:
                        print(resultado.msj_separador)  
            break
        else:
            print(Style.BRIGHT + Fore.RED + '\n¡Aviso! ', Style.BRIGHT + Fore.WHITE + 'La opción' , Style.BRIGHT + Fore.WHITE + str(v_opcion_menu), Style.BRIGHT + Fore.WHITE + ' no es válida, intente de nuevo.')
    # Retorna el delimitador del archivo.
    print(str(resultado.msj_separador_2.format(var=str(resultado.separador))))
    #return v_delimitador
    return resultado

#def udf_solicita_archivo(p_respuesta):
def udf_pide_archivo_s(menu, resultado):
    p_respuesta = resultado.argumentos_menu['opc_2']
    # Importar bibliotecas Python.
    # Importar bibliotecas de las funciones definidas por el usuario. 
    # Se inicializa colorama
    init(autoreset=True)
    # Declaración de variables
    v_resultado = -1
    # Declaracion de la tupla de opciones
    tupla_opciones = ('S','N')
    # Se identica si la acción es limpiar o revisar una fuente de datos.
    if p_respuesta == '1':
        v_accion = 'revisar'
    elif p_respuesta == '2':          
        v_accion = 'limpiar y/o estandarizar'
    elif p_respuesta == '3':          
        v_accion = 'enriquecer'
    elif p_respuesta == '4':
        v_accion = 'utilizar para la busqueda del look up'
    while True:
        # Limpia la consola del usuario
        #limpia_pantalla()
        # Solicita al usuario el nombre del archivo a analizar              
        if not menu:            
            resultado.archivos = input( resultado.msj_nom_archivo.format(var=v_accion)).split(',')                    
        else:
            #resultado.archivos = [ x.nombre for x in menu.archivos]
            resultado.archivos = [ x for x in menu.archivos]        
        # Solicita al usuario la ruta donde se encuentra almacenado el archivo.      
        if not menu:
            resultado.ruta_src = input(resultado.msj_ruta_src).strip()             
        else:
            resultado.ruta_src = menu.ruta_src
        # Solicita al usuario la ruta donde se dejara el archivo.      
        if not menu:
            resultado.ruta_tgt = input(resultado.msj_ruta_tgt).strip()             
        else:
            resultado.ruta_tgt = menu.ruta_tgt
        # Revisa si existe el orígen de datos  / valida rutas si no se conecta a servidor trabaja local               
        #v_archivo = resultado.ruta + archivo                
        flag = udf_ayu_val_ori_datos(menu,resultado)        
        if flag: 
            # Solicitar al usuario el delimitador del archivo. 
            #v_delimitador = udf_delimitador(menu,resultado)
            resultado.ban_exi_ruta = flag
            resultado = udf_delimitador(menu,resultado)
            # Preguntar si el archivo tiene encabezados.
            while True:
                if not menu:
                    v_opcion_header = input(resultado.msj_encabezado).strip().upper()                    
                    resultado.encabezado = True if v_opcion_header=='S' else False                    
                    v_resultado = (v_opcion_header, resultado.encabezado)            
                else:
                    if not menu.archivos==resultado.opc_asterico:

                        v_opcion_header =  'S' if menu.archivos[0].encabezado else 'N'
                        resultado.encabezado = menu.archivos[0].encabezado
                        v_resultado = (v_opcion_header, menu.archivos[0].encabezado) 
                    else:
                        v_opcion_header =  'S' if menu.encabezado else 'N'

                        resultado.encabezado = menu.encabezado
                        v_resultado = (v_opcion_header, menu.encabezado) 
                if v_opcion_header in tupla_opciones:
                    break            
            #v_resultado = (v_opcion_header, menu.archivos[0].encabezado)            
            #v_resultado = (v_archivo, v_opcion_header, v_delimitador)
        elif p_respuesta == '4':
            continue
        else:
            # Se envia el mensaje de que el archivo no existe.
            print(Style.BRIGHT + Fore.RED + '\n¡Atención! ' + Style.BRIGHT + Fore.WHITE + 'la ruta ' + "'" + resultado.ruta_src + "'" + Style.BRIGHT + Fore.WHITE + ' no existe.')
            v_respuesta = input(Style.BRIGHT + Fore.WHITE + "\nPulse la tecla [1] para intentar de nuevo. En caso contrario, pulse otra tecla para regresar al menú principal: ").strip()
            # Si la respuesta es diferente a 1, salimos de la función.
            if v_respuesta == '1':
                continue
        break            
    # Retorna el resultado de la función
    return resultado



def udf_fnt_dato_1(resultado):
    #limpia_pantalla()
    #tupla_archivo =(v_archivo, v_opcion_header, v_delimitador)
    init()
    #genera la lista de objetos Archivo para realizar validaciones con el objeto Resultado
    resultado = udf_ayu_agr_obj_archivos(resultado)
    resultado = udf_ayu_agr_reglas(resultado)
    if resultado != -1:  #tupla_archivo = udf_pide_archivo_s(v_respuesta) = (v_archivo, v_opcion_header, v_delimitador)
        pass
        for idx, archivo  in enumerate(resultado.archivos):
            #complemeta el objeto archivo en rutas
            archivo.ruta_src, archivo.ruta_tgt = resultado.ruta_src, resultado.ruta_tgt            
            #valida que exista el archivo en la ruta
            resultado.ban_exi_archivo=udf_ayu_val_exi_archivo(archivo)
            print(resultado.ban_exi_archivo)
            if resultado.ban_exi_archivo:
                #genera parametria para leer en pyspark para la aplicacion de reglas
                temp_json_par = resultado.as_dict()                
                temp_json_par['archivo'] = archivo.as_dict()  

                print(resultado.msj_trt_archivo , Style.BRIGHT + str(archivo.nombre))#, resultado.reglas)}
                #genera archivo json de parametros para pyspark
                resultado.par_pyspark='{ruta}pars_{var}_{var_1}.json'.format( ruta=resultado.ruta_par_pyspark,var=idx,var_1=archivo.nombre.replace('.csv',''))
                try:
                    with io.open(resultado.par_pyspark,'w',encoding="utf-8") as outfile:
                        print(type(json.loads(json.dumps(temp_json_par))))
                        print(json.loads(json.dumps(temp_json_par)))
                        outfile.write(unicode(json.dumps(temp_json_par, ensure_ascii=False)))
                except Exception as e:
                    with open(resultado.par_pyspark, 'w', encoding='utf-8') as f:
                        json.dump(temp_json_par, f, ensure_ascii=False)

                # se lanza el proceso a pyspark ahi se llevara acabo la limpieza mediante las reglas que sean necesarias
                print(resultado.par_pyspark)
                lan_prc_pyspark(resultado)
                #mensaje de salida a inicio de menu
                input(Style.BRIGHT + Fore.WHITE + "\nPulse la tecla [Enter] para regresar al menú principal ...")
            else:
                print(resultado.msj_trt_archivo_no , Style.BRIGHT + str(resultado.ruta_src) + str(archivo.nombre))#, resultado.reglas)}
































            #lan_prc_pyspark(resultado=resultado)



            #Genera el dataframe de datos del archivo a analizar o limpiar.
            #df_in = udf_gen_dataframe(resultado)
    """
        # Solicitamos al usuario que seleccione un conjunto de campos por revisar o por limpiar junto con las funciones a aplicar.
        if v_respuesta in ('1','2'):
            dict_campos_func = udf_menu_funciones(int(v_respuesta),df_in)                            
        # Solicitamos al usuario que seleccione las columnas que desea generar (enriquecimiento de datos).
        elif v_respuesta == '3':
            dict_campos_func = udf_menu_enriquecimiento(df_in, tupla_archivo[1])
        if len(dict_campos_func) > 0:
            lista_mensaje_salida = [" de salida"]
            if v_respuesta == '1':
                # Ejecuta el proceso principal de validación de datos.
                tupla_resultado = udf_validacion_calidad(df_in, dict_campos_func, tupla_archivo[1])
                lista_mensaje_salida = [" de Registros por Dimensiones de Calidad"," de Estadisticos por Dimensiones de Calidad"]
            elif v_respuesta == '2':
                # Ejecuta el proceso principal de limpieza y de estandarizacion de datos.
                tupla_resultado = udf_limpia_estandariza(df_in, dict_campos_func, tupla_archivo[1])
            elif v_respuesta == '3':
                tupla_resultado = udf_enriquece_datos(df_in, dict_campos_func)
            # Inicializamos el DataFrame para liberar memoria.
            df_in = None
            # Se imprime en pantalla la duración del proceso:
            udf_duracion_proceso(tupla_resultado[1],datetime.now())
            # Se imprime los resultado  en la consola del usuario.
            print(Style.BRIGHT + Fore.YELLOW + '\nResultado  del proceso:\n')
            if v_respuesta == '1':
                print(Style.BRIGHT + Fore.WHITE + 'Salida' + lista_mensaje_salida[0] + ':\n')
            print(tupla_resultado[0])
            # Se muestra en pantalla el reporte de estadísticos.  
            if v_respuesta == '1':
                print()
                print(Style.BRIGHT + Fore.WHITE + 'Salida' + lista_mensaje_salida[1] + ':\n')
                print(tupla_resultado[2])
            # Solicita al usuario si se exportan los resultado  a un archivo.
            udf_exporta_archivo(lista_mensaje_salida, tupla_resultado[0], tupla_resultado[2])
            # Inicializamos la tupla para liberar memoria.
            tupla_resultado = None
            input(Style.BRIGHT + Fore.WHITE + "\nPulse la tecla [Enter] para regresar al menú principal ...")
        else:
            # Inicializamos el DataFrame para liberar memoria.
            df_in = None   
    """