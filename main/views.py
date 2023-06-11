from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def pasta(request):
    return render(request, 'main/pasta.html')

def flour(request):
    return render(request, 'main/flour.html')

def croup(request):
    return render(request, 'main/croup.html')
