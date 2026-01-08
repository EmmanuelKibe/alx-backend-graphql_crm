#!/bin/bash

# 1. Absolute path to your project
PROJECT_DIR="/mnt/c/Users/alemg/OneDrive/Documents/ALX_Pro Dev BE/alx-backend-graphql_crm"

# 2. Path to the LINUX virtual environment python
VENV_PYTHON="$PROJECT_DIR/venv_linux/bin/python3"

# 3. Log file location
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Navigate to project root
cd "$PROJECT_DIR"

# Run the command using the Linux Venv Python
DELETED_COUNT=$("$VENV_PYTHON" manage.py shell -c "
from django.utils import timezone
from crm.models import Customer
from datetime import timedelta
from django.db.models import Max

# Find customers whose most recent order was over a year ago
one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.annotate(
    last_order=Max('order__order_date')
).filter(
    last_order__lt=one_year_ago
)

# Count and delete inactive customers
count = inactive_customers.count()
inactive_customers.delete()
print(count)
")

# Log the result
echo "$(date '+%Y-%m-%d %H:%M:%S') - Deleted $DELETED_COUNT inactive customers" >> "$LOG_FILE"
