import logging
from datetime import datetime
from graphene_django.utils.testing import graphql_query

def log_crm_heartbeat():
    log_file = "/tmp/crm_heartbeat_log.txt"
    timestamp = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    
    # Message to log
    log_message = f"{timestamp} CRM is alive\n"
    
    try:
        # Appending to the file
        with open(log_file, "a") as f:
            f.write(log_message)
            
        #Perform a simple GraphQL query to ensure the API is responsive
        from alx-backend-graphql_crm.schema import schema
        result = schema.execute('{ hello }')
        
        if result.errors:
            with open(log_file, "a") as f:
                f.write(f"{timestamp} - GraphQL Error: {result.errors}\n")
                
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - System Error: {str(e)}\n")