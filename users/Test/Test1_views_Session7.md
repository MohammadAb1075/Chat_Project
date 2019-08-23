from datetime import datetime
from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse

from users.models import User

def user_list_view(request):
    users= User.objects.all()
    return render(
        request,
        "userlist7.html",
        {
            "users" : users
        }
    )


def user_list_json_view(request):
    user_list=[]
    for u in User.objects.all():
        user_list.append(
            {
                'first_name': u.first_name,
                'last_name' : u.last_name,
                'birthday'  : u.birthday,
            }
        )
    # pprint(user_list)
    return JsonResponse(
        {
            "users" : user_list
        }
    )
