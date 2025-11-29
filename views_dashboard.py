from django.shortcuts import render

def home(request):
    return render(request, "index_home.html")

def dashboard_home(request):
    return render(request, "dashboard_index.html")