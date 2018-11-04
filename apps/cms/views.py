from django.shortcuts import render

def cms_login(request):
    return render(request, 'cms/login.html')
