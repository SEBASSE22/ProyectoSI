from django.shortcuts import render

def login(request):
    data = {
        'title': 'Log In',
    }
    return render(request, 'login/login.html', data)