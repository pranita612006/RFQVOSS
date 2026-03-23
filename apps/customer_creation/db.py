# db.py
from .models import CustomerInfo

def get_customer_details(customer_id):
    """
    Fetch name and search_name for a given customer_id.
    Returns a dictionary or None if not found.
    """
    try:
        customer = CustomerInfo.objects.get(customer_id=customer_id)
        print("DEBUG:", customer_id, customer)
        return {
            "name": customer.name,
            "search_name": customer.search_name
        }
    except CustomerInfo.DoesNotExist:
        return None
