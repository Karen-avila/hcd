################################################################################ UDF register
import sys, os, datetime
from dateutil.parser import parse

def is_date(string, fuzzy=False):
    try:
      parse(str(string), fuzzy=fuzzy)
      return True
    except ValueError:
      return False
def aplly_fmt(value, fmt):
    try:
        if not is_date(value):
            return value
        else:
            return parse(value, fuzzy=True).strftime(fmt)
    except:
      return value
# udf que se registra en el sql context para la validacion de fechas
def cadena_to_date2(value, fmt):
  value=str(value)
  date = None
  if value.isdigit():
    date= aplly_fmt(value, fmt)
  else:
    date= aplly_fmt(value, fmt)
  return date
# udf que se registra en el sql context para la inserccion de fecha de procesamineto
def fecha_proceso():
  return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# udf que se registra en el sql context para la el split de  nombres regla generica
def parse_name(p_nombre):
    val_cad_full_name=p_nombre
    if (val_cad_full_name)=='':
        get_nom_parser=add_Lista(None, None, None, None,"None")
    else:
        len_palabras = palabras_longitud(val_cad_full_name)
        palabras = split_palabras(val_cad_full_name)
        num_palabras = total_nombre(palabras)
        if (num_palabras > 6):
            if (valida_nombre(len_palabras, (3,3,1,3,3,1), (False, False,True,False, False,True))):
                if (valida_articulo(palabras, (True,True, False,True,True, False))):
                    segundo_nombre = palabras[1:(num_palabras-6)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre ,palabras[-6]+' '+palabras[-5]+' '+palabras[-4] ,palabras[-3]+' '+palabras[-2]+' '+palabras[-1],"6,1")
        if (num_palabras > 5):
            if (valida_nombre(len_palabras, (3,1,3,3,1), (False,True,False, False,True))):
                if (valida_articulo(palabras,(True, False,True,True, False))):
                    segundo_nombre = palabras[1:(num_palabras-5)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre ,palabras[-5]+' '+palabras[-4] ,palabras[-3]+' '+palabras[-2]+' '+palabras[-1],"5,1")
            if (valida_nombre(len_palabras, (3,3,1,3,1), (False, False, True, False, True))):
                if (valida_articulo(palabras, (True, True, False, True, False))):
                    segundo_nombre = palabras[1:(num_palabras - 5)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-5] + ' ' + palabras[-4]+ ' ' +palabras[-3], palabras[-2] + ' ' + palabras[-1],"5,2")
        if (num_palabras > 4):
            if (valida_nombre(len_palabras, (3,1,3,1), (False,True, False,True))):
                if (valida_articulo(palabras,(True, False,True, False))):
                    segundo_nombre = palabras[1:(num_palabras-4)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre ,palabras[-4]+' '+palabras[-3] ,palabras[-2]+' '+palabras[-1],"4+,1")
            if (valida_nombre(len_palabras, (1, 3, 3, 1), (True, False, False, True))):
                if (valida_articulo(palabras,(False, True, True, False))):
                    segundo_nombre = palabras[1:(num_palabras - 4)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-4] ,palabras[-3] + ' ' + palabras[-2] + ' ' + palabras[-1],"4+,2")
            if (valida_nombre(len_palabras, (3, 3, 1, 1), (False, False, True, True))):
                if (valida_articulo(palabras, (True, True, False, False))):
                    segundo_nombre = palabras[1:(num_palabras - 4)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-4] + ' ' + palabras[-3] + ' ' + palabras[-2], palabras[-1],"4+,3")
            if (valida_nombre(len_palabras, (1, 1, 3, 1), (True, True, False, True))):
                if (valida_articulo(palabras,(False, False, True, False))):
                    segundo_nombre = palabras[1:(num_palabras - 3)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-3] , palabras[-2]+ ' ' + palabras[-1],"4+,4")
            if (valida_nombre(len_palabras, (1, 3, 1, 1), (True, False, True, True))):
                if (valida_articulo(palabras,(False, True, False, False))):
                    segundo_nombre = palabras[1:(num_palabras - 3)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-3]+ ' ' + palabras[-2], palabras[-1],"4+,5")
            if (valida_nombre(len_palabras, (1, 1, 1), (True, True, True))):
                if (valida_articulo(palabras, (False, False, False))):
                    segundo_nombre = palabras[1:(num_palabras - 2)]
                    segundo_nombre = ' '.join(segundo_nombre)
                    get_nom_parser=add_Lista(palabras[0], segundo_nombre, palabras[-2], palabras[-1],"4+,6")
        if (num_palabras == 4):

            if (valida_nombre(len_palabras, (3, 3, 1), (False, False, True))):
                if (valida_articulo(palabras, (True, True, False))):
                    get_nom_parser=add_Lista(palabras[0], '', palabras[1] + ' ' + palabras[2] + ' ' + palabras[3],'',"4,1")
            if (valida_nombre(len_palabras, (1, 3, 1), (True, False, True))):
                if (valida_articulo(palabras, (False, True, False))):
                    get_nom_parser=add_Lista(palabras[0], '', palabras[1], palabras[2] + ' ' + palabras[3],"4,2")
            if (valida_nombre(len_palabras, (3, 1, 1), (False, True, True))):
                if (valida_articulo(palabras, (True, False, False))):
                    get_nom_parser=add_Lista(palabras[0], '', palabras[1]  + ' ' + palabras[2] ,palabras[3],"4,3")
            if (valida_nombre(len_palabras, (1, 1, 1), (True, True, True))):
                if (valida_articulo(palabras, (False, False, False))):
                    get_nom_parser=add_Lista(palabras[0], palabras[1], palabras[2], palabras[3],"4,4")
        if (num_palabras == 3):
            if (valida_nombre(len_palabras, (3, 1), (False, True))):
                if (valida_articulo(palabras, (True, False))):
                    get_nom_parser=add_Lista(palabras[0], None, palabras[1] + ' ' + palabras[2], None,"3")
            get_nom_parser=add_Lista(palabras[0], None, palabras[1], palabras[2],"3,1")
        if (num_palabras == 2):
            get_nom_parser=add_Lista(palabras[0], None, palabras[1], None,"2")
        if (num_palabras == 1):
            get_nom_parser=add_Lista(palabras[0], None, None, None,"1")
    return get_nom_parser
def add_Lista(nombre,segundo_nombre,paterno, materno, call=None):
    if call:
        pass
    lis_nombre=""
    lis_nombre+=str(nombre) if nombre else ", "
    lis_nombre+=", "+str(segundo_nombre) if segundo_nombre else ", "
    lis_nombre+=", "+str(paterno) if paterno else ", "
    lis_nombre+=", "+str(materno) if materno else ", "
    return lis_nombre
def valida_nombre(len_palabras,log_palabras,mayor_menor):
    len_pal = len(len_palabras) - 1
    for idx, val_mayor_menor in reversed(list(enumerate(mayor_menor))):
        if val_mayor_menor:
            if len_palabras[len_pal] >= log_palabras[idx]:
                check_longitud_palabra = True
            else:
                check_longitud_palabra = False
                break
        else:
            if len_palabras[len_pal] <= log_palabras[idx]:
                check_longitud_palabra = True
            else:
                check_longitud_palabra = False
                break
        len_pal = len_pal - 1
    return check_longitud_palabra
def valida_articulo(palabras, posicion_articulo):
    lista_articulos=['y','los','de','del','san','la','DE','DEL','SAN','LOS','Y','LA']
    len_pal = len(palabras) - 1
    for idx, val_articulo in reversed(list(enumerate(posicion_articulo))):
        if val_articulo:
            if palabras[len_pal] in lista_articulos:
                check_longitud_palabra = True
            else:
                check_longitud_palabra = False
                break
        else:
            if palabras[len_pal] not in lista_articulos:
                check_longitud_palabra = True
            else:
                check_longitud_palabra = False
                break
        len_pal = len_pal - 1
    return check_longitud_palabra
def palabras_longitud(val_cad_full_name):
    return list(map(len, val_cad_full_name.split()))
def split_palabras(val_cad_full_name):
    return val_cad_full_name.split()
def total_nombre(len_palabras):
    return len(len_palabras)
