import quda.core.schema
import quda.quda.schema
import quda.prfl.schema

import graphene

class Query(
        quda.core.schema.Query,
        quda.quda.schema.Query,
        quda.prfl.schema.Query,
        graphene.ObjectType
    ):
    pass

class Mutation(
        quda.core.schema.Mutation,
        quda.quda.schema.Mutation,
        quda.prfl.schema.Mutation,
        graphene.ObjectType
    ):
    pass

class Subscription(
        quda.core.schema.Subscription,
        quda.prfl.schema.Subscription,
        graphene.ObjectType
    ):
    pass

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription
)
