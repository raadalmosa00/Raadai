from django.contrib import admin
from django.urls import path
from . import views_dashboard, views_accounts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views_dashboard.home, name="home"),
    path("login/", views_accounts.login_view, name="login"),
    path("register/", views_accounts.register_view, name="register"),
    path("dashboard/", views_dashboard.dashboard_home, name="dashboard"),
]