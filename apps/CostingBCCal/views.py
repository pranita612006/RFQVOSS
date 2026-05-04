from django.shortcuts import render
from config.decorators import require_active_customer

@require_active_customer
def CostingBCCal_form(request):
    return render(request, "CostingBCCal/CostingBCCal_form.html")

