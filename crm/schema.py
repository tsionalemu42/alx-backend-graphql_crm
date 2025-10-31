import graphene
from graphene_django.types import DjangoObjectType
from crm.models import Customer, Order
from customers.models import Customer
from sales.models import Order


# Define GraphQL object types
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone")

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id", "customer", "product", "amount", "status", "created_at")

# Define the root Query
class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    all_orders = graphene.List(OrderType)

    def resolve_all_customers(root, info):
        return Customer.objects.all()

    def resolve_all_orders(root, info):
        return Order.objects.all()

# Create the schema
schema = graphene.Schema(query=Query)
