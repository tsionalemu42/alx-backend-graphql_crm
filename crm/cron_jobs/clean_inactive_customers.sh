#!/bin/bash

# Navigate to the Django project root directory
cd "$(dirname "$0")/../.."

# Define log file path
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Run Django shell command to delete inactive customers
deleted_count=$(python3 manage.py shell -c "
from datetime import timedelta
from django.utils import timezone
from crm.models import Customer

one_year_ago = timezone.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(last_order_date__lt=one_year_ago).delete()
print(deleted)
")

# Log with timestamp
timestamp=$(date '+%Y-%m-%d %H:%M:%S')
echo \"$timestamp - Deleted $deleted_count inactive customers\" >> \"$LOG_FILE\"
