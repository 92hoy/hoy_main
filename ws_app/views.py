from django.shortcuts import render


# Create your views here.
def socket_test(request):
    context = {}
    return render(request, 'socket_test.html', context)
