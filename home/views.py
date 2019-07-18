from django.shortcuts import render


# Create your views here.
def sign(request):
    return render(request, 'sign/sign.html')


def main(request):
    return render(request, 'main/main.html')
