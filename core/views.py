from django.shortcurts import render


def home(request):
    return render(request,'home.html')