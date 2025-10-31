#!/bin/bash

# Navigate to the Django project root
cd "$(dirname "$0")/../.."

# Run the Django shell command to delete inactive customers (no orders since a year ago)
deleted_count=$(python3 manage.py shell -c "
from datetime import timedelta
from django.utils import timezone
from customers.models import Customer
one_year_ago = timezone.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(last_order_date__lt=one_year_ago).delete()
print(deleted)
")

# Log the result with timestamp
timestamp=$(date '+%Y-%m-%d %H:%M:%S')
echo \"$timestamp - Deleted $deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt
