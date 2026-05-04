from django.shortcuts import render
from config.decorators import require_active_customer

@require_active_customer
def BlanketSales_form(request):
    return render(request, "BlanketSales/BlanketSales_form.html")
