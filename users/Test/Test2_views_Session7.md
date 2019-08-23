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


def user_list_item_view(request):

    if request.method == 'GET':
        user_list=[]
        users=User.objects
        if 'first_name' in request.GET:
            users=users.filter(first_name=request.GET['first_name'])

        if 'last_name' in request.GET:
            users=users.filter(last_name=request.GET['last_name'])

        else:
            users=users.all()

        for u in users:
            # print(type(u.number_of_friends))
            user_list.append(
                {
                    'first_name': u.first_name,
                    'last_name' : u.last_name,
                    'id'  : u.id,
                }
            )

        # pprint(user_list)


        return JsonResponse(
            {
                "users" : user_list
            }
        )
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        number_of_friends=request.POST['number_of_friends']
        print(len(first_name))
        if len(first_name) > 20:

            return JsonResponse(
                {
                    'message' : 'First Name Max Length is 20'
                },
                status = 400
            )

        try:
            number_of_friends = int(number_of_friends)
        except ValueError:
            return JsonResponse(
                {
                    'message' : 'Number Of Friends is a IntegerField'
                },
                status = 400
            )
        birthday = datetime.fromisoformat(birthday)

        print(type(number_of_friends))
        u=User(
            # **request.POST
            first_name = first_name,
            last_name = last_name,
            birthday = birthday,
            number_of_friends=number_of_friends
        )
        u.save()

        return JsonResponse(
    {
        "users" :{
            'first_name': u.first_name,
            'last_name' : u.last_name,
            'id'  : u.id,
        }
    }
)
