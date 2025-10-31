import graphene
from crm.models import Order

class OrderType(graphene.ObjectType):
    id = graphene.ID()
    customer_email = graphene.String()
    order_date = graphene.DateTime()

class Query(graphene.ObjectType):
    recent_orders = graphene.List(OrderType, days=graphene.Int())

    def resolve_recent_orders(root, info, days=7):
        from datetime import datetime, timedelta
        cutoff = datetime.now() - timedelta(days=days)
        return Order.objects.filter(order_date__gte=cutoff)

schema = graphene.Schema(query=Query)
