from quda.core.modelsBase import *
from django.apps import apps

class BaseRule(ModelBase):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    def __str__(self):
        return "BaseRule {0}".format(self.id)
    def getRule(self, name):
        return apps.get_model('clng', name)

class TrimRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'trim'
    def getName(self):
        return 'TRIM'
    def getDescription(sel):
        return 'Quita espacios entre cadena'
    def getExample(self):
        return '"Hola   mundo" => "Hola mundo"'

class LtrimRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'ltrim'
    def getName(self):
        return 'LTRIM'
    def getDescription(sel):
        return 'Quita espacios a la izquierda de la cadena'
    def getExample(self):
        return '"  Hola mundo" => "Hola mundo"'

class RtrimRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'rtrim'
    def getName(self):
        return 'RTRIM'
    def getDescription(sel):
        return 'Quita espacios a la derecha de la cadena'
    def getExample(self):
        return '"Hola mundo    " => "hola mundo"'

class UpperRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'upper'
    def getName(self):
        return 'MAYUS'
    def getDescription(sel):
        return 'Convierte todas las letras de una cadena a mayusculas'
    def getExample(self):
        return '"Hola mundo    " => "HOLA MUNDO"'

class LowerRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'lower'
    def getName(self):
        return 'MINUS'
    def getDescription(sel):
        return 'Convierte todas las letras de una cadena a minusculas'
    def getExample(self):
        return '"Hola Mundo" => "hola mundo"'

class InitCapRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'icap'
    def getName(self):
        return 'INITCAP'
    def getDescription(sel):
        return 'Convierte a mayuscula la primera letra de cada palabra en una cadena'
    def getExample(self):
        return '"hola mundo. saludos!." => "Hola Mundo. Saludos!."'

class LengthRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'len'
    def getName(self):
        return 'LENGTH'
    def getDescription(sel):
        return 'Regresa una nueva columna con el numero de carateres que contiene una columna'
    def getExample(self):
        return '"hola mundo. saludos!." => "21"'

class ParserNamedRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'pname'
    def getName(self):
        return 'PARSERNAME'
    def getDescription(sel):
        return 'Realiza la segmentacion de una cadena que contiene un nombre completo a nombre , segundo nombre, apellido paterno y materno'
    def getExample(self):
        return '"Jose Alfredo Marquez Gutierrez" => "Jose", "Alfredo", "Marquez", "Gutierrez"'

class CleanAllRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return 'clean'
    def getName(self):
        return ''
    def getDescription(sel):
        return 'Aplica la regla TRIM y MINUS a todos los campos'
    def getExample(self):
        return '"*"'

class ToIntegerRule(BaseRule):
    pass
    def apply(self, value):
        return value
    def getCode(self):
        return '2int'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class SubstringMatchRule(BaseRule):
    patron = models.CharField(max_length=200)
    def apply(self, value):
        return value
    def getCode(self):
        return 'submatch'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''
    def getExample(self):
        return 'patron="mundo" : "Hola mundo" => "hola "'

class SubstringRule(BaseRule):
    init = models.IntegerField(default=0)
    end = models.IntegerField(default=0)
    def apply(self, value):
        return value
    def getCode(self):
        return 'substr'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class FormatDecimalRule(BaseRule):
    decimal = models.IntegerField(default=0)
    def apply(self, value):
        return value
    def getCode(self):
        return 'formatfloat'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class RpadRule(BaseRule):
    length = models.IntegerField(default=0)
    caracter = models.CharField(default='')
    def apply(self, value):
        return value
    def getCode(self):
        return 'rpad'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class LpadRule(BaseRule):
    length = models.IntegerField(default=0)
    caracter = models.CharField(default='')
    def apply(self, value):
        return value
    def getCode(self):
        return 'lpad'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class ReplaceCaracterRule(BaseRule):
    search = models.CharField(default=0)
    replace = models.CharField(default='')
    def apply(self, value):
        return value
    def getCode(self):
        return 'repchar'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class ReplaceWordRule(BaseRule):
    search = models.CharField(default=0)
    replace = models.CharField(default='')
    def apply(self, value):
        return value
    def getCode(self):
        return 'repword'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class DateFprmatRule(BaseRule):
    inputFormat = models.CharField(default ='dd/MM/yyyy')
    outputFormat = models.CharField(default ='yyyyMMdd')
    def apply(self, value):
        return value
    def getCode(self):
        return 'dateformat'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''

class ToDateRule(BaseRule):
    outputFormat = models.CharField(default ='%m/%d/%Y')
    def apply(self, value):
        return value
    def getCode(self):
        return 'date2str'
    def getName(self):
        return ''
    def getDescription(sel):
        return ''
