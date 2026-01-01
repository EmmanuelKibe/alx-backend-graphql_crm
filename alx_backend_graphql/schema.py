import graphene
from crm.schema import CRMQuery, Mutation as CRMutation  # Import the query and mutation from your app

# We inherit from CRMQuery and graphene.ObjectType to combine them
class Query(CRMQuery, graphene.ObjectType):
    pass

class Mutation(CRMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
