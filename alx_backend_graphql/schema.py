import graphene

class Query(graphene.ObjectType):
    # Define the field 'hello' as a String
    hello = graphene.String()

    # The resolver function returns the data for the 'hello' field
    def resolve_hello(root, info):
        return "Hello, GraphQL!"

# Create the schema object
schema = graphene.Schema(query=Query)
