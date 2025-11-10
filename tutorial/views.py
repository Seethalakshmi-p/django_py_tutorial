from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def java_script(request):
    return render(request, 'java_script.html')

def django(request):
    return render(request, 'django.html')


def fast_api(request):
    return render(request, 'fast_api.html')


def program(request):
    return render(request, 'program.html')

def flask(request):
    return render(request, 'flask.html')