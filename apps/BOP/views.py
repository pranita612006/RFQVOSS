from django.shortcuts import render
from config.decorators import require_active_customer

@require_active_customer
def BOP_form(request):
    return render(request, "BOP/BOP_form.html")
