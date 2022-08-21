from ariadne import QueryType, make_executable_schema

from ariadne import gql

type_defs = gql("""
    type Query {
        hello: String!
        hi:String!
    }
""")

query = QueryType()


@query.field("hello")
def resolve_hello(*_):
    return "Hello world!"


@query.field("hi")
def resolve_hi(_, info):
    request = info.context["request"]
    user_agent = request.headers.get("user-agent", "guest")
    return "Hello, %s!" % user_agent

# schema = make_executable_schema(type_defs, query)
# app = GraphQL(schema, debug=True)


schema = make_executable_schema(type_defs, query)
