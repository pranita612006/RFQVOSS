from apps.customer_creation.models import CustomerInfo

def get_customer_details(customer_id: str):
    try:
        customer = CustomerInfo.objects.get(customer_id=customer_id)
        return {
            "name": customer.name,
            "search_name": customer.search_name
        }
    except CustomerInfo.DoesNotExist:
        return None