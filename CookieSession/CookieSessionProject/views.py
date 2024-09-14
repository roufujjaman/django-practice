from django.shortcuts import render
from datetime import datetime, timedelta

def set_cookie(request, ckey, cval, days=None):
    if days == None:
        response = render(request, 'cookie.html', {
            'action': 'SETTING COOKIE [set_cookie]'
        })
        response.set_cookie(ckey, cval)
        return response
    else:
        response = render(request, 'cookie.html', {
            'action': f'SETTING COOKIE FOR {days} DAYS [set_cookie_days]'
        })
        response.set_cookie(ckey, cval, expires=datetime.now()+timedelta(days=days))
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

def set_session(request, username, language):
    data = {
        'username': username,
        'lanuage': language
    }
    request.session.update(data)
    return render(request, 'session.html', {
        'action': 'SESSION CREATED'
    })

def get_session(request):
    data = request.session.items
    return render(request, 'session.html', {
        'action': 'SESSION DATA',
        'session': data
    })

def delete_session(request):
    request.session.flush()
    return render(request, 'session.html', {
        'action': 'SESSION FLUSHED'
    })