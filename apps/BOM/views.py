from django.shortcuts import render
from config.decorators import require_active_customer

@require_active_customer
def BOM_form(request):
    return render(request, "BOM/BOM_form.html")
