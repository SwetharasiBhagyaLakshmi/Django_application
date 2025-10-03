from django.shortcuts import render

def signup_view(request):
    return render(request, 'accounts/signup.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
