from django.shortcuts import render
from django.utils import timezone

print(">>> LOADING apps.pages.views <<<")

def index(request):
    return render(request, 'pages/index.html')


def erp_data_view(request):
    current_date = timezone.now().strftime("%d-%b-%y")
    return render(request, 'pages/erp_data.html', {"current_date": current_date})


def upload_data_view(request):
    return render(request, "pages/upload_data.html")


def user_management_view(request):
    return render(request, "pages/user_management.html")


# ✅ ADD THESE DASHBOARD VIEWS

def dashboard_v1(request):
    return render(request, 'pages/dashboard_v1.html')

def dashboard_v2(request):
    return render(request, 'pages/dashboard_v2.html')

def dashboard_v3(request):
    return render(request, 'pages/dashboard_v3.html')