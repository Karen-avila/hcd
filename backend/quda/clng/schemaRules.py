from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
from .modelsRules import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ColumnInput(graphene.InputObjectType):
    index = graphene.Int(description="Index de campo")
    name = graphene.String(description="nombre del campo")

#################################################################
class BaseRuleInput(graphene.InputObjectType):
    apply_rule = graphene.Boolean(required=False, default_value=True, description="")
#################################################################
class TrimRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Quita espacios entre cadena"
#################################################################
class LtrimRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Quita espacios a la izquierda de la cadena"
#################################################################
class SubstringRuleInput(BaseRuleInput):
    init = graphene.Int(description="Pocicion inicial de donde se quiere extraer")
    end = graphene.Int(description="Pocicion final de donde se quiere extraer")
class RtrimRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Quita espacios a la derecha de la cadena"
class UpperRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Convierte todas las letras de una cadena a mayusculas"
class LowerRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Convierte todas las letras de una cadena a minusculas"
class InitCapRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Convierte a mayuscula la primera letra de cada palabra en una cadena"
class LengthRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Regresa una nueva columna con el numero de carateres que contiene una columna"

class ParserNamedRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Realiza la segmentacion de una cadena que contiene un nombre completo a nombre , segundo nombre, apellido paterno y materno"
class CleanAllRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Aplica la regla TRIM y MINUS a todos los campos"
class ToIntegerRuleInput(BaseRuleInput):
    pass
    class Meta:
        description ="Convierte una cadena o numero a entero, puede truncar datos decimales"
class SubstringMatchRuleInput(BaseRuleInput):
    patron = graphene.String(required=False, default_value='', description="Cadena que se buscara en un cadena como pocosion inicial de donde se quiere extraer")
    class Meta:
        description ="Regresa la palabra buscada y el resto de la cadena"
class FormatDecimalRuleInput(BaseRuleInput):
    decimal = graphene.Int(description="Numero de decimales")
    class Meta:
        description ="Realiza la precision de decimales"
class RpadRuleInput(BaseRuleInput):
    length = graphene.Int(description="Numero de la longitud de la cadena que se desea completar con determinado caracter")
    caracter = graphene.String(required=False, default_value='', description="Caracter de reemplazo")
    class Meta:
        description ="Completa una cadena con determinado caracter con una longitud especifica hacia la derecha"
class LpadRuleInput(BaseRuleInput):
    length = graphene.Int(description="Numero de la longitud de la cadena que se desea completar con determinado caracter")
    caracter = graphene.String(required=False, default_value='', description="Caracter de reemplazo")
    class Meta:
        description ="Completa una cadena con determinado caracter con una longitud especifica hacia la izquierda"
class ReplaceCaracterRuleInput(BaseRuleInput):
    search = graphene.String(required=False, default_value='', description="lista de caracteres separados por coma")
    replace = graphene.String(required=False, default_value='', description="Caracter de reemplazo, puede ser vacio ''")
    class Meta:
        description ="Elimina uno o varios caracteres en una cadena"
class ReplaceWordRuleInput(BaseRuleInput):
    search = graphene.String(required=False, default_value='' ,  description="lista de palabras separados por coma")
    replace = graphene.String(required=False, default_value='',  description="lista de palabraa a remplazar separados por coma")
    class Meta:
        description ="Realiza el remplazo de una palabra por otra en una cadena\
                      \nEjemplo\
                      \n'search: word1,word2'\
                      \n'replace: palabra1,palabra2'\
                      \n -- word1 se reemplaza por palabra1 \n   y word2 se remplaza por palabra2\
                      "
class DateFormatRuleInput(BaseRuleInput):
    inputFormat = graphene.String(required=False, default_value='', description="Formato de actual de la columna  ejemplo ")
    outputFormat = graphene.String(required=False, default_value='', description="Formato de salida de la columna ejmplo ")
    class Meta:
        description ="Realiza el cambio de formato de fecha \
                      \n Ejemplo: inputFormat='dd/MM/yyyy' , outputFormat='yyyyMMdd': '09/01/2020' => '20200109'    "
class ToDateRuleInput(BaseRuleInput):
    outputFormat = graphene.String(required=False, default_value='')
    class Meta:
        description ="Convierte una cadena a fecha\
                      \n Ejemplo: outputFormat='%m/%d/%Y': '09-05-2020' => '09/05/2020'"

#################################################################
class ColumnsinRulesInput(graphene.InputObjectType):
    columns = graphene.List(ColumnInput, required=False, description="Columnas a las que se aplicara la regla")
    lpadRule  = graphene.Field( LpadRuleInput , required=False)
    rpadRule  = graphene.Field( RpadRuleInput , required=False)
    trimRule = graphene.Field(TrimRuleInput, required=False,)
    ltrimRule = graphene.Field(LtrimRuleInput, required=False,)
    substringRule = graphene.Field(SubstringRuleInput, required=False)
    rtrimRule  = graphene.Field( RtrimRuleInput , required=False)
    upperRule  = graphene.Field( UpperRuleInput , required=False)
    lowerRule  = graphene.Field( LowerRuleInput , required=False)
    initCapRule  = graphene.Field( InitCapRuleInput , required=False)
    lengthRule  = graphene.Field( LengthRuleInput , required=False)
    parserNamedRule  = graphene.Field( ParserNamedRuleInput , required=False)
    cleanAllRule  = graphene.Field( CleanAllRuleInput , required=False)
    toIntegerRule  = graphene.Field( ToIntegerRuleInput , required=False)
    substringMatchRule  = graphene.Field( SubstringMatchRuleInput , required=False)
    formatDecimalRule  = graphene.Field( FormatDecimalRuleInput , required=False)
    replaceCaracterRule  = graphene.Field( ReplaceCaracterRuleInput , required=False)
    replaceWordRule  = graphene.Field( ReplaceWordRuleInput , required=False)
    dateFormatRule  = graphene.Field( DateFormatRuleInput , required=False)
    toDateRule  = graphene.Field( ToDateRuleInput , required=False)
    class Meta:
        description ="Configuracion de reglas que se aplicara las columnas"
