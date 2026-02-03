from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model  

User = get_user_model()


def login_view(request):
    error_login = None
    if request.method == "POST" and 'login_submit' in request.POST:
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            error_login = "Username yoki parol xato"
    context={
        'error_login': error_login, 
        'show_form': 'login'
    }
    return render(request, 'account/login.html', context=context)


def register_view(request):
    print(request.POST)
    error_register = None
    if request.method == "POST" and 'register_submit' in request.POST:
        username = request.POST.get('register_username')
        email = request.POST.get('register_email')
        password = request.POST.get('register_password')
        password2 = request.POST.get('register_password2')

        if password != password2:
            error_register = "Parollar mos emas"
        elif User.objects.filter(username=username).exists():
            error_register = "Username allaqachon mavjud"
        elif User.objects.filter(email=email).exists():
            error_register = "Email allaqachon mavjud"
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
    context={
        'error_register': error_register, 
        'show_form': 'register'
    }
    return render(request, 'account/login.html', context=context)



def logout_view(request):
    logout(request)
    return redirect('login')
