import graphene
import crm.schema  # Ensure this import is correct

# Your main Query class MUST inherit from crm.schema.Query
class Query(crm.schema.Query, graphene.ObjectType):
    pass

class Mutation(crm.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)