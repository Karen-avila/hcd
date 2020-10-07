# -*- coding: utf-8 -*-
############################################################################################
# Nombre del programa: main_standardization_cleaning.py                                    #
# Descripción: Programa principal de estandarización y limpieza de datos.                  #
# Autor: CRDM para Softtek.                                                                #
# Fecha de creación: 23/06/2020.                                                           #
# Parametros de entrada: No aplica.                                                        #
# Retorna: La plantilla con los resultado  de la validación o limpieza.                    #
# Modificó: No aplica.                                                                     #
# Fecha de última modificación: No aplica.                                                 #
# Descripción de la última modificación: No aplica.                                        #
############################################################################################
# Importar bibliotecas Python.

import gc
from datetime import datetime
from colorama import Style, init, Fore


from menu.obj.obj_clases       import Resultado
from menu.udf.udf_archivo      import udf_pide_archivo_s, udf_fnt_dato_1
from menu.menu_opciones        import menu_opc_inicio,menu_val_opc_1,menu_val_opc_2
"""
from udf_genera_dataframe     import udf_genera_dataframe
from udf_menu_funciones       import udf_menu_funciones
from udf_limpia_estandariza   import udf_limpia_estandariza
from udf_duracion_proceso     import udf_duracion_proceso
from udf_exporta_archivo      import udf_exporta_archivo
from udf_validacion_calidad   import udf_validacion_calidad
from udf_menu_enriquecimiento import udf_menu_enriquecimiento
from udf_enriquece_datos      import udf_enriquece_datos
"""

def menu_general(menu=None):    
    # Importar funciones personalizadas.
    # Inicializamos la biblioteca colorama
    resultado      = Resultado()
    tupla_opciones = ('0','1','2','3')        

    init()
    # Declaración de la lista de opciones del menú.
    while True:
        # Muestra el menú de opciones.
        menu_opc_inicio()
        # Solicita al usuario la opción deseada.
        resultado  , v_respuesta= menu_val_opc_1(menu,resultado )        
        # valida respuesta             
        if v_respuesta not in tupla_opciones:
            input(resultado.alerta_1)
        else:
            # Salimos de la aplicación si la opción es igual a 0.
            if v_respuesta == '0':
                break
            else:
                # Le preguntamos al usuario el tipo de fuente de datos que desea revisar o limpiar.
                if not(menu):
                    resultado  = menu_val_opc_2(menu, resultado)
                    v_resp_fuente_datos = resultado.argumentos_menu['opc_2']
                else:
                    resultado.argumentos_menu['opc_2'] = str(menu.argumentos_menu['opc_2'])
                    v_resp_fuente_datos  = resultado.argumentos_menu['opc_2']
                # Si la fuente de datos por analizar es un archivo.
                if v_resp_fuente_datos == '1':
                    # Solicitamos al usuario que ingrese el nombre del archivo.                                        
                    #tupla_archivo = udf_pide_archivo_s(v_respuesta) = (v_archivo, v_opcion_header, v_delimitador)
                    #tupla_archivo = udf_pide_archivo_s(menu, resultado)
                    resultado = udf_pide_archivo_s(menu, resultado)
                    # Revisa si el usuario proporcionó un archivo y si indicó si este tiene encabezado o no.
                    udf_fnt_dato_1 (resultado)

                    break

                # Si la fuente de datos por analizar es una base de datos.
                elif v_resp_fuente_datos == '2':     
                    input(Style.BRIGHT + Fore.WHITE + '\nModulo en construcción.\n' + Style.BRIGHT + Fore.WHITE + 'Pulse la tecla [Enter] para regresar al menú principal ...')
    print('\nGracias por usar la aplicación. Tenga un excelente día.')

