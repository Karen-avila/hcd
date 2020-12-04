from quda.core.modelsBase import *

VARS = {
    'model': 'BaseRule',
    'name': 'BaseRule',
    'plural': 'BaseRule',
}
class BaseRule(ModelBase):
    pass
    class Meta():
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def getClassName(self):
            return self.__class__.__name__

VARS = {
    'model':'TrimRule',
    'name':'TrimRule',
    'plural':'TrimRules'
}
class TrimRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
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

VARS = {
    'model':'LtrimRule',
    'name':'LtrimRule',
    'plural':'LtrimRules'
}
class LtrimRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
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

VARS = {
    'model':'RtrimRule',
    'name':'RtrimRule',
    'plural':'RtrimRules'
}
class RtrimRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'rtrim'
    def getName(self):
        return 'RTRIM'
    def getDescription(self):
        return 'Quita espacios a la derecha de la cadena'
    def getExample(self):
        return '"Hola mundo    " => "hola mundo"'

VARS = {
    'model':'UpperRule',
    'name':'UpperRule',
    'plural':'UpperRules'
}
class UpperRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'upper'
    def getName(self):
        return 'MAYUS'
    def getDescription(self):
        return 'Convierte todas las letras de una cadena a mayusculas'
    def getExample(self):
        return '"Hola mundo    " => "HOLA MUNDO"'

VARS = {
    'model':'LowerRule',
    'name':'LowerRule',
    'plural':'LowerRules'
}
class LowerRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'lower'
    def getName(self):
        return 'MINUS'
    def getDescription(self):
        return 'Convierte todas las letras de una cadena a minusculas'
    def getExample(self):
        return '"Hola Mundo" => "hola mundo"'

VARS = {
    'model':'InitCapRule',
    'name':'InitCapRule',
    'plural':'InitCapRules'
}
class InitCapRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'icap'
    def getName(self):
        return 'INITCAP'
    def getDescription(self):
        return 'Convierte a mayuscula la primera letra de cada palabra en una cadena'
    def getExample(self):
        return '"hola mundo. saludos!." => "Hola Mundo. Saludos!."'

VARS = {
    'model':'LengthRule',
    'name':'LengthRule',
    'plural':'LengthRules'
}
class LengthRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'len'
    def getName(self):
        return 'LENGTH'
    def getDescription(self):
        return 'Regresa una nueva columna con el numero de carateres que contiene una columna'
    def getExample(self):
        return '"hola mundo. saludos!." => "21"'

VARS = {
    'model':'ParserNamedRule',
    'name':'ParserNamedRule',
    'plural':'ParserNamedRules'
}
class ParserNamedRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'pname'
    def getName(self):
        return 'PARSERNAME'
    def getDescription(self):
        return 'Realiza la segmentacion de una cadena que contiene un nombre completo a nombre , segundo nombre, apellido paterno y materno'
    def getExample(self):
        return '"Jose Alfredo Marquez Gutierrez" => "Jose", "Alfredo", "Marquez", "Gutierrez"'

VARS = {
    'model':'CleanAllRule',
    'name':'CleanAllRule',
    'plural':'CleanAllRules'
}
class CleanAllRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'clean'
    def getName(self):
        return ''
    def getDescription(self):
        return 'Aplica la regla TRIM y MINUS a todos los campos'
    def getExample(self):
        return '"*"'

VARS = {
    'model':'ToIntegerRule',
    'name':'ToIntegerRule',
    'plural':'ToIntegerRules'
}
class ToIntegerRule(BaseRule):
    pass
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return '2int'
    def getName(self):
        return 'TOINT'
    def getDescription(self):
        return 'Convierte una cadena o numero a entero, puede truncar datos decimales'
    def getExample(self):
        return '"78.09" => "78"'

VARS = {
    'model':'SubstringMatchRule',
    'name':'SubstringMatchRule',
    'plural':'SubstringMatchRules'
}
class SubstringMatchRule(BaseRule):
    patron = models.CharField(max_length=200,blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'submatch'
    def getName(self):
        return 'SUBMATCH'
    def getDescription(self):
        return 'Regresa la palabra buscada y el resto de la cadena'
    def getExample(self):
        return 'patron="mundo" : "Hola mundo, Saludos!" => "mundo, Saludos!"'

VARS = {
    'model':'SubstringRule',
    'name':'SubstringRule',
    'plural':'SubstringRules'
}
class SubstringRule(BaseRule):
    init = models.IntegerField(default=0,blank=False)
    end = models.IntegerField(default=0,blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'substr'
    def getName(self):
        return 'SUBSTR'
    def getDescription(self):
        return ''
    def getExample(self):
        return 'patron="mundo" : "Hola mundo, Saludos!" => "mundo, Saludos!"'

VARS = {
    'model':'FormatDecimalRule',
    'name':'FormatDecimalRule',
    'plural':'FormatDecimalRules'
}
class FormatDecimalRule(BaseRule):
    decimal = models.IntegerField(default=0,blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'formatfloat'
    def getName(self):
        return 'FLOAT'
    def getDescription(self):
        return 'Realiza la precision de decimales'
    def getExample(self):
        return 'precision=3 : "4324,98730000" => "4324,987"'

VARS = {
    'model':'RpadRule',
    'name':'RpadRule',
    'plural':'RpadRules'
}
class RpadRule(BaseRule):
    length = models.IntegerField(default=0,blank=False)
    caracter = models.CharField(max_length=500,default='',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'rpad'
    def getName(self):
        return 'RPAD'
    def getDescription(self):
        return 'Comleta una cadena con determinado caracter con una longitud especifica hacia la derecha'
    def getExample(self):
        return 'longitud=10 , caracter="?": "mexico" => "mexico????"'

VARS = {
    'model':'LpadRule',
    'name':'LpadRule',
    'plural':'LpadRules'
}
class LpadRule(BaseRule):
    length = models.IntegerField(default=0,blank=False)
    caracter = models.CharField(max_length=500,default='',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'lpad'
    def getName(self):
        return 'LPAD'
    def getDescription(self):
        return 'Comleta una cadena con determinado caracter con una longitud especifica hacia la izquierda'
    def getExample(self):
        return 'longitud=10 , caracter="?": "mexico" => "mexico????"'

VARS = {
    'model':'ReplaceCaracterRule',
    'name':'ReplaceCaracterRule',
    'plural':'ReplaceCaracterRules'
}
class ReplaceCaracterRule(BaseRule):
    search = models.CharField(max_length=500,default=0,blank=False)
    replace = models.CharField(max_length=500,default='',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'repchar'
    def getName(self):
        return 'REPCHAR'
    def getDescription(self):
        return 'elimina uno o varios caracteres en una cadena'
    def getExample(self):
        return 'caracter=["$","%","/"] , remplazo="z": "$signo de pesos con %porcentaje y una division/ => "zsigno de pesos con zporcentaje y una divisionz"'

VARS = {
    'model':'ReplaceWordRule',
    'name':'ReplaceWordRule',
    'plural':'ReplaceWordRules'
}
class ReplaceWordRule(BaseRule):
    search = models.CharField(max_length=500,default='',blank=False)
    replace = models.CharField(max_length=500,default='',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'repword'
    def getName(self):
        return 'REPWORD'
    def getDescription(self):
        return 'realiza el remplazo de una palabro por otra en una cadena'
    def getExample(self):
        return 'busqueda="Ave." , remplazo="Avenida": "Ave. Miguel Aleman, colonia Universidad" => "Avenida Miguel Aleman, colonia Universidad"'

VARS = {
    'model':'DateFormatRule',
    'name':'DateFormatRule',
    'plural':'DateFormatRules'
}
class DateFormatRule(BaseRule):
    inputFormat = models.CharField(max_length=50,default ='dd/MM/yyyy',blank=False)
    outputFormat = models.CharField(max_length=50,default ='yyyyMMdd',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'dateformat'
    def getName(self):
        return 'DTFORMAT'
    def getDescription(self):
        return 'realiza el cambio de formato de fecha'
    def getExample(self):
        return 'formato_entrada="dd/MM/yyyy" , formato_de_salida="yyyyMMdd": "09/01/2020" => "20200109"'

VARS = {
    'model':'ToDateRule',
    'name':'ToDateRule',
    'plural':'ToDateRules'
}
class ToDateRule(BaseRule):
    outputFormat = models.CharField(max_length=50,default ='%m/%d/%Y',blank=False)
    class Meta(ModelBase.Meta):
        verbose_name = VARS['name']
        verbose_name_plural = VARS['plural']
        permissions = MakePermissions(VARS)
    def apply(self, value):
        return value
    def getCode(self):
        return 'str2date'
    def getName(self):
        return 'STRTODATE'
    def getDescription(self):
        return 'Convierte una cadena a fecha'
    def getExample(self):
        return 'formato_de_salida="%m/%d/%Y": "09-05-2020" => "09/05/2020"'
