# apps/customer_creation/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import CustomerInfo
from .db import get_customer_details

def customer_form(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        name = request.POST.get("name")
        search_name = request.POST.get("search_name")

        return redirect(
            f"/item_creation/?customer_id={customer_id}&name={name}&search_name={search_name}"
        )

    customer_ids = CustomerInfo.objects.values_list("customer_id", flat=True)
    search_names = CustomerInfo.objects.values_list("search_name", flat=True)
    return render(request, "customer_creation/customer_form.html", {
        "customer_ids": customer_ids,
        "search_names": search_names,
    })

def get_customer_info(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
    elif request.method == "GET":
        customer_id = request.GET.get("customer_id")
    else:
        return HttpResponseNotAllowed(["GET", "POST"])

    details = get_customer_details(customer_id)
    return JsonResponse(details or {})
