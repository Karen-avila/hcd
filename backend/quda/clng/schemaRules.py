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
    apply_rule = graphene.Boolean(required=False, default_value=True)

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

#################################################################
class ColumnsinRulesInput(graphene.InputObjectType):
    columns = graphene.List(ColumnInput, required=False)
    trimRule = graphene.Field(TrimRuleInput, required=False)
    ltrimRule = graphene.Field(LtrimRuleInput, required=False)
    substringRule = graphene.Field(SubstringRuleInput, required=False)
