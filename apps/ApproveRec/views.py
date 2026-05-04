from django.shortcuts import render
from config.decorators import require_active_customer

@require_active_customer
def ApproveRec_form(request):
    return render(request, "ApproveRec/ApproveRec_form.html")
