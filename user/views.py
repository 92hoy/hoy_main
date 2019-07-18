from django.shortcuts import render


# Create your views here.

def user_info(request):
    return render(request, 'user/user_info.html')
