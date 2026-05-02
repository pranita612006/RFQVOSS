from django.contrib import admin
from django.urls import include, path
from apps.pages import views as page_views   # ✅ IMPORTANT

urlpatterns = [

    # ✅ DASHBOARD URLS (PUT AT TOP — VERY IMPORTANT)
    path('dashboard/v1/', page_views.dashboard_v1, name='dashboard_v1'),
    path('dashboard/v2/', page_views.dashboard_v2, name='dashboard_v2'),
    path('dashboard/v3/', page_views.dashboard_v3, name='dashboard_v3'),

    # EXISTING
    path("", include("apps.opportunities.urls")), 
    path('', include('apps.pages.urls')),
    path('', include('apps.dyn_dt.urls')),
    path('', include('apps.dyn_api.urls')),
    path('charts/', include('apps.charts.urls')),
    path("admin/", admin.site.urls),
    path("", include('admin_adminlte.urls')),
    path("", include("apps.todo.urls")),
    path("", include("apps.customer_creation.urls")),
    path("", include("apps.item_creation.urls")),
    path("", include("apps.feasibility_form.urls")),
    path("", include("apps.BOM.urls")),
    path("", include("apps.BOP.urls")),
    path("", include("apps.BOC.urls")),
    path("", include("apps.CostingBCCal.urls")),
    path("", include("apps.BlanketSales.urls")),
    path("", include("apps.ApproveRec.urls")),
    path("", include("apps.Report.urls")),
]