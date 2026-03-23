from django.urls import path
from . import views

urlpatterns = [
    path("customer_creation/", views.customer_form, name="customer_creation"),
    path("get_customer_info/", views.get_customer_info, name="get_customer_info"),
]

