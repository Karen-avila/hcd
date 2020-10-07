import sys, os, datetime

from dateutil.parser import parse



# udf que se registra en el sql context para la validacion de fechas
def is_date(string, fuzzy=False):
    try:
      parse(string, fuzzy=fuzzy)
      return True
    except ValueError:
      return False


# udf que se registra en el sql context para la validacion de fechas
def cadena_to_date(value):
  date = None
  if value.isdigit():
    date=value
  else:
    try:
      if not is_date(value):
        date =value
      else:
        date = parse(value, fuzzy=True).strftime('%d/%m/%Y-%H:%M:%S.%f')
    except:
      date = value
  return date

# udf que se registra en el sql context para la inserccion de fechas
def fecha_proceso():
  return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ ('.0')
