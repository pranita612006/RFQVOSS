from django.urls import path
from . import views

urlpatterns = [
   path("feasibility_form/", views.feasibility, name="feasibility_form"),
   path("feasibility/create/", views.feasibility_create, name="feasibility_create"),
   path("feasibility/list/", views.feasibility_list, name="feasibility_list"),
   path("get_opportunity_data/", views.get_opportunity_data, name="get_opportunity_data"),
]