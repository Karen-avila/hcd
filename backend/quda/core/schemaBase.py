from django.apps import apps
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django import DjangoObjectType
from rx import Observable
from graphene_subscriptions.events import CREATED, UPDATED, DELETED
from django_filters import FilterSet, OrderingFilter

import graphene

class BaseNode(DjangoObjectType):
    getProperties = graphene.String(source='getProperties')
    class Meta:
        abstract = True
    @classmethod
    def sortBy(cls, queryset, info):
        try:
            for argument in info.field_asts[0].arguments:
                if argument.name.value == 'sort':
                    return queryset.order_by(argument.value.value)
        except:
            pass
        return queryset

class ConnectionBase(graphene.relay.Connection):
    total_count = graphene.Int()
    class Meta:
        abstract = True
    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()

class ModelVar(graphene.ObjectType):
    properties = graphene.types.json.JSONString(
            app = graphene.String(),
            model = graphene.String()
        )
    def resolve_properties(parent, info, *args, **kwargs):
        return apps.get_model(kwargs['app'], kwargs['model']).VARS
def resolve_modelVar(parent, info):
    return {}
