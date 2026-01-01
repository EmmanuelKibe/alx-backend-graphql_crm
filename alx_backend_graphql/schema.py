import graphene
from crm.schema import CRMQuery  # Import the query from your app

# We inherit from CRMQuery and graphene.ObjectType to combine them
class Query(CRMQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
