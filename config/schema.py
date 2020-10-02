import quda.core.schema
import quda.quda.schema

import graphene

class Query(
        quda.core.schema.Query,
        graphene.ObjectType
    ):
    pass

class Mutation(
        quda.core.schema.Mutation,
        quda.quda.schema.Mutation,
        graphene.ObjectType
    ):
    pass

class Subscription(
        quda.core.schema.Subscription,
        graphene.ObjectType
    ):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)
