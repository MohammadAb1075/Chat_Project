from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from users.models import User
from users.serializers import RequestGetSerializer, UserSerializer


def user_list_view(request):
    users = User.objects.all()
    return render(
        request,
        "userlist7.html",
        {
            "users" : users
        }
    )


def user_list_item_view(request):

    if request.method == 'GET':

        request_serializer = RequestGetSerializer(data=request.GET)

        if request_serializer.is_valid():
            users = User.objects
            # if request_serializer.data['first_name']:
            if 'first_name' in request_serializer.data:
                users = users.filter(
                    first_name=request_serializer.data['first_name']
                )
            if 'last_name' in request_serializer.data:
            # if request_serializer.data['last_name']:
                users = users.filter(
                    last_name=request_serializer.data['last_name']
                )
            serializer=UserSerializer(instance=users,many=True)
            return JsonResponse(
                {
                    "users" : serializer.data
                }
            )

        else:
            return JsonResponse(
                request_serializer.errors, status=400
            )




    elif request.method == 'POST':
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
            serializer.save()

        else:
            return JsonResponse(
                serializer.errors,status=400
            )

        return JsonResponse({
        "user" : serializer.data
    })
