class ActiveCustomerMiddleware:
    """
    Middleware to attach the active customer directly to the request object.
    This allows easy access to request.active_customer in any view.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Attach the customer dictionary directly to the request object
        request.active_customer = {
            'id': request.session.get('active_customer_id'),
            'name': request.session.get('active_customer_name'),
            'search_name': request.session.get('active_customer_search_name'),
        }
        
        # Helper boolean
        request.has_active_customer = bool(request.active_customer['id'])

        response = self.get_response(request)
        return response
