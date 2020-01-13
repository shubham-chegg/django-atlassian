from django.shortcuts import render
import requests

auth_code_dict = {}


def get_access_token(code):
    url = "https://tutorschatdomain.auth.us-west-2.amazoncognito.com/oauth2/token"

    payload = "grant_type=authorization_code&code={}&client_id=k49sm93943rj71uvo0vmhfoe0&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F".format(code)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic azQ5c205Mzk0M3JqNzF1dm8wdm1oZm9lMDp0N25wcGxyODkzYWwyZWViMTVkc2wzMWNmbDExdWw4ZmhoNWR0YWNmNHRmdnB1ZG1ucWw=",
        'cache-control': "no-cache",
        'Postman-Token': "59ed3261-2949-4f21-a8f3-f2cf7f3a3192"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.status_code)
    print(response.json())
    if response.status_code == 200:
        return response.json()

    return {}


def get_user_info(access_token):
    url = "https://tutorschatdomain.auth.us-west-2.amazoncognito.com/oauth2/userInfo"

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer {}".format(access_token),
        'Accept': "*/*",
        'Host': "tutorschatdomain.auth.us-west-2.amazoncognito.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "153",
        'Cookie': "XSRF-TOKEN=628851d4-6420-4f45-b35d-78b0cb290416",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.json())
    if response.status_code == 200:
        return response.json()

    return {}


def get_tutor_page(request):
    print(request)
    code = request.COOKIES.get('code')

    if not code:
        auth_code = request.GET.get("code")
        auth_code_dict[auth_code] = get_access_token(auth_code)
        if not auth_code_dict[auth_code]:
            return render(request, 'user_info.html', {"user_info" : {}})
    else:
        auth_code = code

    user_info = get_user_info(auth_code_dict[auth_code]['access_token'])
    response = render(request, 'user_info.html', {})
    # if not code:
    #     response.set_cookie("code", auth_code)
    return response


def logout(request):
    response = render(request, 'user_info.html', {"user_info" : {}})
    response.delete_cookie("code")
    return response


import json
import jwt

from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def installed(request):
    """
    Main view to handle the signal of the cloud instance when the addon
    has been installed
    """
    try:
        post = json.loads(request.body)
        key = post['key']
        shared_secret = post['sharedSecret']
        client_key = post['clientKey']
        host = post['baseUrl']
    except Exception:
        return HttpResponse(status=201)

    print(post)
    print(key)
    print(shared_secret)
    print(client_key)
    print(host)

    return HttpResponse(status=204)