from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def LoginView(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username, password=password)
        if user is None:
            user = User.objects.get(email=email, password=password)
            if user is None:
                messages.error(request, 'Incorrect informations!')
                return redirect('Login')
            
        Login(user)
        return redirect('#')
    
    return render(request, 'Accounts/login.html')
