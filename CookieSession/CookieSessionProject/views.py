from django.shortcuts import render


def set_cookie(request, ckey, cval, days=3):
    response = render(request, 'cookie.html', {
        'action': 'SETTING COOKIE [set_cookie]'
    })
    response.set_cookie(ckey, cval)
    return response

def get_cookie(request):
    cookies = request.COOKIES
    return render(request, 'cookie.html', {
        'action': 'GETTING COOKIE [get_cookie]',
        'cookies': cookies
    })

def delete_cookie(request, name):
    response = render(request, 'cookie.html', {
        'action': 'COOKIE DELETED'
    })
    response.delete_cookie(name)
    return response


def default(request, name='roufujjaman'):
    return render(request, 'cookie.html', {
        'action': name
    })