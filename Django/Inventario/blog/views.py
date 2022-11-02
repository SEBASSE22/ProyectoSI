from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'blog/login.html')

def saludo(request):
    return render(request, 'blog/saludo.html')