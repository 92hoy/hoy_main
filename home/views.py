from django.shortcuts import render


# Create your views here.

def main_base(request):
    return render(request, 'main_base/main_base.html')
