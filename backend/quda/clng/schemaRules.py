from quda.core.schemaBase import *
from quda.core.schema import UserNode
from .models import *
from .modelsRules import *

#################################################################
#########   TYPES or NODES   ####################################
#################################################################
class ColumnInput(graphene.InputObjectType):
    index = graphene.Int()
    name = graphene.String()

#################################################################
class BaseRuleInput(graphene.InputObjectType):
    column = graphene.List(ColumnInput)

#################################################################
class TrimRuleInput(BaseRuleInput):
    pass

#################################################################
class LtrimRuleInput(BaseRuleInput):
    pass

#################################################################
class SubstringRuleInput(BaseRuleInput):
    init = graphene.Int()
    end = graphene.Int()

class ColumnsinRulesInput(graphene.InputObjectType):
    columns = graphene.List(ColumnInput, required=False)
    trimRules = graphene.List(TrimRuleInput, required=False)
    ltrimRules = graphene.List(LtrimRuleInput, required=False)
    substringRules = graphene.List(SubstringRuleInput, required=False)
