#!/usr/bin/env python3
import requests
from datetime import datetime, timedelta

# Define endpoint and query
url = "http://localhost:8000/graphql"
query = """
{
  orders {
    id
    orderDate
    customer {
      email
    }
  }
}
"""

try:
    # Send the GraphQL request
    response = requests.post(url, json={"query": query})
    response.raise_for_status()
    data = response.json()

    # Get current time and last 7 days
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    # Open log file
    with open("/tmp/order_reminders_log.txt", "a") as log:
        log.write(f"\n--- Order Reminder Log ({today}) ---\n")

        # Loop through orders
        for order in data.get("data", {}).get("orders", []):
            order_date_str = order.get("orderDate")
            if not order_date_str:
                continue

            # Parse order date
            try:
                order_date = datetime.fromisoformat(order_date_str)
            except Exception:
                continue

            # Filter for orders within the last 7 days
            if order_date >= week_ago:
                order_id = order["id"]
                email = order["customer"]["email"]
                log.write(f"Order ID: {order_id}, Email: {email}\n")

        log.write("---- End of Log ----\n")

    print("Order reminders processed!")

except Exception as e:
    print(f"Error: {e}")
