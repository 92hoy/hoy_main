# -*- coding: utf-8 -*-
import simplejson
import urllib.request
import urllib
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse


# Create your views here.
def sign(request):

    print(3333)
    return render(request, 'sign/sign.html')


def login(request):
    if request.is_ajax():
        id = request.POST.get('login_id')
        password = request.POST.get('login_pw')
        print('id', id)
        print('password', password)
        return JsonResponse({"a":"b"})
    return render(request, 'sign/login.html')


def logout(request):
    print('logout')
    return JsonResponse({'return': 'success'})


def api_bit(request):
    bit = ['BTC', 'ETH', 'EOS']
    # API_HOST = list()
    bit_data = {}
    for a in bit:
        # API_HOST.append('https://api.bithumb.com/public/ticker/' + a)
        b = urllib.request.urlopen('https://api.bithumb.com/public/ticker/' + a)
        c = simplejson.load(b)
        print('c',c)
        c['coin'] = a
        bit_data[a] = c

        # BTC_API_HOST = 'https://api.bithumb.com/public/ticker/BTC'
        # ETH_API_HOST = 'https://api.bithumb.com/public/ticker/ETH'
        # EOS_API_HOST = 'https://api.bithumb.com/public/ticker/EOS'

        # u = urllib.request.urlopen(BTC_API_HOST)
        # u = urllib.request.urlopen(ETH_API_HOST)
        # u = urllib.request.urlopen(EOS_API_HOST)
        # data = simplejson.load(u)
        # print(data['data'])
        # data = u.read()
        # print(data)
        # context = {'bit_data': bit_data}

    return JsonResponse(bit_data)


def main(request):
    # context = {'bit_data': api_bit(request)}
    # print(context)
    context = {}
    return render(request, 'main/main.html', context)
