#!/bin/bash

# Navigate to the project root where manage.py lives
# This ensures the script finds the Django settings
cd "$(dirname "$0")/../.."

# Define the log file path
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Run the Django shell command
# We use 'shell -c' to run the Python logic directly
DELETED_COUNT=$(python3 manage.py shell -c "
from django.utils import timezone
from crm.models import Customer
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)
# Filter customers with no orders since a year ago and delete them
deleted, _ = Customer.objects.filter(order__date__lt=one_year_ago).distinct().delete()
print(deleted)
")

# Log the result with a timestamp
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $DELETED_COUNT inactive customers" >> "$LOG_FILE"
