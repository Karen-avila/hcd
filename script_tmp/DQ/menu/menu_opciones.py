# -*- coding: utf-8 -*-
############################################################################################
# Nombre de la función: udf_menu_opciones.py                                               #
# Descripción: Función que muestra en pantalla el menú de opciones del programa            #
#              principal.                                                                  #
# Autor: CRDM para Softtek.                                                                #
# Fecha de creación: 23/06/2020.                                                           #
# Parametros de entrada de la función: No aplica.                                          #
# Retorna: El menú de opciones de la aplicación.                                           #
# Modificó: No aplica.                                                                     #
# Fecha de última modificación: No aplica.                                                 #
# Descripción de la última modificación: No aplica.                                        #
############################################################################################
import os,sys
import sys  
from menu.udf.udf_ayuda import limpia_pantalla
from colorama import Style, Fore, init

def menu_opc_inicio():  
  # Importar bibliotecas Python.
  # Se inicializa colorama.
  init(autoreset=True)
  # Limpia la consola del usuario
  limpia_pantalla()
  # Se inicializan las varibales de la función
  v_char_marco   = Style.BRIGHT + Fore.YELLOW + chr(35)
  v_char_espacio = chr(32)
  v_linea_horizontal = v_char_marco * 76
  v_linea_vertical   = v_char_marco + (v_char_espacio * 74) + v_char_marco
  v_encabezado_01    = v_char_marco + Style.BRIGHT + Fore.WHITE + ' Bienvenido al Módulo de Limpieza y Estandarización de Datos versión 1.0' + (v_char_espacio * 2) + v_char_marco
  v_encabezado_02    = v_char_marco + Style.BRIGHT + Fore.WHITE + ' Creado por Softtek en el año 2020.' + (v_char_espacio * 39) + v_char_marco
  # Se inicializa el listado del menú
  lista_menu = [v_linea_horizontal, v_linea_vertical, v_encabezado_01, v_encabezado_02, v_linea_vertical, v_linea_horizontal,
                '\n', Style.BRIGHT + Fore.CYAN + 'Opciones del menú principal:', '\n', Style.BRIGHT + Fore.YELLOW + '1. Validación de Datos.', 
                Style.BRIGHT + Fore.YELLOW + '2. Limpieza y Estandarización de Datos.', Style.BRIGHT + Fore.YELLOW + '3. Enriquecimiento de Datos.',
                Style.BRIGHT + Fore.YELLOW + '0. Salir de la aplicación.', '\n'] 
  # Muestra en pantalla el encabezado y la lista de opciones
  for i in range(len(lista_menu)):
      print(lista_menu[i])
  return True




def menu_val_opc_1(menu,resultado):
    if not menu:
        resultado.argumentos_menu['opc_1'] = str(input(resultado.msj_0))
    else:
        resultado.argumentos_menu['opc_1'] = str(menu.argumentos_menu['opc_1'])
    return resultado, resultado.argumentos_menu['opc_1']


def menu_val_opc_2(menu,resultado):
    tupla_opciones = ('0','1','2')
    p_respuesta= resultado.argumentos_menu['opc_1']
    # Se inicializa colorama.
    init(autoreset=True)
    # Se identica si la acción es limpiar o revisar una fuente de datos.
    if p_respuesta == '1':
        v_accion = 'Revisar '
    elif p_respuesta == '2':          
        v_accion = 'Limpiar y Estandarizar '
    elif p_respuesta == '3':          
        v_accion = 'Enriquecer '
    # Se inicializa el listado del menú.
    lista_menu = [Style.BRIGHT + Fore.CYAN + '\n¿Qué desea hacer?', '\n', Style.BRIGHT + Fore.YELLOW + '1. ' + v_accion + 'un Archivo.', 
                  Style.BRIGHT + Fore.YELLOW + '2. ' + v_accion + 'una Base de Datos.', Style.BRIGHT + Fore.YELLOW + '0. Regresar al Menú Principal.', '\n'] 
    # Se incializa tupla de opciones validas. 
    while True:
        # Limpia la consola del usuario
        limpia_pantalla()
        # Muestra en pantalla la lista de opciones
        for opcion in lista_menu:
            print(opcion)
        # Solicita al usuario seleccionar una opción.
        if not menu:
          resultado.argumentos_menu['opc_2'] = str(input(resultado.msj_1))
        else:
          resultado.argumentos_menu['opc_2'] = str(menu.argumentos_menu['opc_2'])
        # Revisa que la respuesta del usuario sea válida.
        if resultado.argumentos_menu['opc_2'] not in tupla_opciones:
            input(resultado.alerta_1)
        else:
            break        
    return resultado  


"""


def udf_menu_opciones_formato_fecha():

    v_opciones_formato_fecha = { 'formato_entrada':None
                                 ,'formato_salida':None
                                }

    v_for_fecha= { 1 :'%d/%m/%Y' ,5 :'%d-%m-%Y' ,9 :'%Y/%m/%d'
                  ,2 :'%d/%m/%y' ,6 :'%d-%m-%y' ,10 :'%y/%m/%d'
                  ,3 :'%m/%d/%Y' ,7 :'%m-%d-%Y' ,11 :'%Y-%m-%d'
                  ,4 :'%m/%d/%y' ,8 :'%m-%d-%y' ,12 :'%y-%m-%d'
                 }

    print('\n' + "      ***Opciones de formato de entrada***"
               + '\n' + "1. dd/mm/yyyy    5.  dd-mm-yyyy   9. yyyy/mm/dd"
               + '\n' + "2. dd/mm/yy      6.  dd-mm-yy     10. yy/mm/dd"
               + '\n' + "3. mm/dd/yyyy    7.  mm-dd-yyyy   11. yyyy-mm-dd"
               + '\n' + "4  mm/dd/yy      8.  mm-dd-yy     12. yy-mm-dd"+'\n'
         )

    while True:
         v_opcion_fecha_entrada = str(input("Seleccione el formato de entrada de la fecha: "))
         try:
            v_opciones_formato_fecha['formato_entrada'] = v_for_fecha[int(v_opcion_fecha_entrada)]
            break
         except:
             print('\n'+"Opcion incorrecta, intente de nuevo.")
             continue

    v_formato_fecha_salida = str(input('\n'+"***Opciones de formato de salida***"
                                      +'\n'+"   dd/dia    dd->02,  dia->Lunes"
                                      +'\n'+"   mm/mes    mm->01,  mes->Enero"
                                      +'\n'+"   yy/yyyy   yy->20, yyyy->2020"
                                    +'\n\n'+"Introduzca el formato de salida en el que quiere la fecha: "
                                      ))

    v_formato_fecha_salida = v_formato_fecha_salida.replace("dd", "%d")
    v_formato_fecha_salida = v_formato_fecha_salida.replace("dia", "%A")
    v_formato_fecha_salida = v_formato_fecha_salida.replace("mm", "%m")
    v_formato_fecha_salida = v_formato_fecha_salida.replace("mes", "%B")
    v_formato_fecha_salida = v_formato_fecha_salida.replace("yyyy", "%Y")
    v_formato_fecha_salida = v_formato_fecha_salida.replace("yy", "%y")

    v_opciones_formato_fecha['formato_salida'] = v_formato_fecha_salida

    return v_opciones_formato_fecha

def udf_menu_opciones_formato_decimal():

    v_opciones_formato_escala = {'formato_escala': None}

    while True:
       try:
          v_escala = int(input("Introduzca el numero de digitos decimales: "))
          if(v_escala>=0 and v_escala>=28):
              raise
          v_opciones_formato_escala['formato_escala'] = '{:.'+str(v_escala)+'f}'
          break
       except:
          print('\n' + "Opcion incorrecta el rango debe ser entre 0 y 28, intente de nuevo: ")
          continue

    return v_opciones_formato_escala
    
def udf_menu_opciones_formato_numero():

    v_opciones_formato_numero = {'formato_numero':None}

    v_formato_numero = str(input("Introduzca el formato de los numeros: "))
    v_opciones_formato_numero['formato_numero'] = v_formato_numero

    return v_opciones_formato_numero
    
def udf_menu_opciones_cadena_to_entero():

    v_opciones_formato_decimal = {'formato_decimal': None}

    print('\n' + "***Opciones de formato***"
        + '\n' + "      1. Truncar"
        + '\n' + "      2. Redondear" '\n'
          )

    while True:
       try:
          v_decimal = int(input("Selecciona una opcion para la parte decimal: "))
          if(v_decimal<=0 or v_decimal>=3):
              raise
          v_opciones_formato_decimal['formato_decimal'] = v_decimal
          break
       except:
          print('\n' + "Opcion incorrecta, las opciones validas son 1 o 2, intente de nuevo: ")
          continue

    return v_opciones_formato_decimal

def udf_menu_opciones_cadena_to_pad():

    v_opciones_lpad = { 'longitud': None
                       ,'caracter': None
                       }

    while True:
       try:
          v_longitud = int(input("Introduzca la longitud: "))
          if(v_longitud<=0 or v_longitud>1000):
              raise
          v_opciones_lpad['longitud'] = v_longitud
          break
       except:
          print('\n' + "Opción incorrecta, la longitud debe estar entre 0 y 1000 intente de nuevo. ")
          continue

    v_opciones_lpad['caracter'] = str(input("Introduzca el caracter: "))

    return v_opciones_lpad 
    
def udf_menu_opciones_cadena_to_substring():

    v_opciones_substring= { 'inicio': None
                           ,'longitud':None
                          }
    while True:
       try:
          v_inicio = int(input("Selecciona la posicion de inicio: "))
          #if(v_inicio<=0): # CRDM 17/08/2020.
          if(v_inicio<0): # CRDM 17/08/2020. 
              raise
          v_opciones_substring['inicio'] = v_inicio
          break
       except:
          print('\n' + "Opcion incorrecta, el inicio debe ser un entero positivo, intente de nuevo: ")
          continue

    while True:
        try:

            v_longitud = str(input("Seleccione la longitud: "))
            if (v_longitud !=''):
               v_longitud = int(v_longitud)
               if (v_longitud <= 0):
                  raise
               else: v_longitud = v_longitud + v_inicio
            else: v_longitud = None
            v_opciones_substring['longitud'] = v_longitud
            break
        except:
            print('\n' + "Opcion incorrecta, la longitud debe ser un entero positivo, intente de nuevo: ")
            continue

    return v_opciones_substring
    
def udf_menu_opciones_cadena_is_igual():

    v_opciones_is_igual = { 'cadena': None
                          }

    v_busqueda = str(input("Introduzca el valor de la busqueda: "))
    v_opciones_is_igual['cadena'] = v_busqueda

    return v_opciones_is_igual

def udf_menu_opciones_cadena_ocurrencia():

    v_opciones_ocurrencia = { 'cadena': None
                                ,'numero_ocurrencia': None
                               }

    v_busqueda_cadena = str(input("Introduzca el valor de la busqueda: "))
    v_opciones_ocurrencia['cadena'] = v_busqueda_cadena

    while True:
       try:
          v_numero_ocurrencia = int(input("Selecciona el numero de la ocurrencia: "))
          v_opciones_ocurrencia['numero_ocurrencia'] = v_numero_ocurrencia
          break
       except:
          print('\n' + "Opción incorrecta, el numero de la ocurrencia debe ser entero. ")
          continue

    return v_opciones_ocurrencia

def udf_menu_opciones_is_length():

    v_opciones_is_length = { 'longitud': None
                           }
    while True:
       try:
          v_length = int(input("Introduzca la longitud de la cadena a buscar: "))
          v_opciones_is_length['longitud'] = v_length
          break
       except:
          print('\n' + "Opción incorrecta, la longitud debe ser entero. ")
          continue

    return v_opciones_is_length
    
def udf_menu_opciones_cadena_replace_2():

    v_opciones_cadena_replace = { 'cadena_busqueda': None
                                 ,'numero_ocurrencia': None
                                }

    v_busqueda_cadena = str(input("Introduzca el valor de la busqueda: "))
    v_opciones_cadena_replace['cadena_busqueda'] = v_busqueda_cadena

    v_busqueda_reemplazo = str(input("Introduzca el valor del reemplazo: "))
    v_opciones_cadena_replace['cadena_reemplazo'] = v_busqueda_reemplazo

    return v_opciones_cadena_replace
    
def udf_menu_opciones_cadena_replace(busqueda, sustitucion):

    v_opciones_cadena_replace = { 'cadena_busqueda': None
                                 ,'numero_ocurrencia': None
                                }

    
    v_opciones_cadena_replace['cadena_busqueda'] = busqueda

    
    v_opciones_cadena_replace['cadena_reemplazo'] = sustitucion

    return v_opciones_cadena_replace
    


def udf_menu_opciones_cadena_fecha():

    v_opciones_cadena_fecha = {'formato_entrada':None
                              ,'formato_salida':None}

    v_opciones_cadena_fecha['formato_entrada'] = str(input("Introduzca el formato de entrada de la cadena: "))
    v_opciones_cadena_fecha['formato_salida'] = str(input("Introduzca el formato de salida de la fecha: "))

    return v_opciones_cadena_fecha

def udf_menu_opciones_look_up():

    import pandas as pd
    from udf_solicita_archivo import udf_solicita_archivo
    from udf_genera_dataframe import udf_genera_dataframe

    v_opciones_lookup = {'catalogo_source':None
                        ,'nombre_busqueda':None
                        ,'nombre_retorno':None
                         }

    dict_opc_campos = {}
    tupla_archivo = udf_solicita_archivo('4')
    p_df_in = udf_genera_dataframe(tupla_archivo[0], tupla_archivo[1], tupla_archivo[2])

    for i in range(len(p_df_in.columns)):
        dict_opc_campos[str(i)] = p_df_in.columns[i]

    lista_keys_campos = dict_opc_campos.keys()
    v_opciones_campos = str(dict_opc_campos).replace('{', '').replace('}', '').replace(':', '.').replace("'", '') + '.'

    print('\n' + v_opciones_campos)

    while True:
        campo_join = input("Seleccione el campo con el cual se realizara la busqueda: ")
        if campo_join not in lista_keys_campos:
            print('Respuesta invalida, intente de nuevo.')
        else: break

    while True:
        campo_retorno = input("Seleccione el campo de retorno: ")
        if campo_retorno not in lista_keys_campos:
            print('Respuesta invalida, intente de nuevo.')
        elif campo_join == campo_retorno:
            print('El campo de retorno debe ser diferente al campo de la búsqueda, intente de nuevo.')
        else:
            break

    v_opciones_lookup['nombre_busqueda'] = dict_opc_campos[campo_join]
    v_opciones_lookup['nombre_retorno']  = dict_opc_campos[campo_retorno]

    p_columna_busqueda = p_df_in[dict_opc_campos[campo_join]]
    p_columna_retorno = p_df_in[dict_opc_campos[campo_retorno]]

    lista_registros_catalogo =[]

    for i in range(len(p_columna_busqueda)):
       val_columna_busqueda= p_columna_busqueda.values[i]
       val_columna_retorno = str(p_columna_retorno.values[i])

       if pd.isna(val_columna_busqueda):
          lista_registros_catalogo += [['','']]
       else:
          lista_registros_catalogo += [[val_columna_busqueda,val_columna_retorno]]

    v_opciones_lookup['catalogo_source'] = lista_registros_catalogo

    return v_opciones_lookup
"""