from datetime import datetime
from django.http import JsonResponse

from users.models import User
from users.serializers import UserSerializer


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
        request_serializer = RequestGetSerializer(data=request.GET)
        if request_serializer.is_valid():

            users = Users.objects
            if request_serializer.data['first_name']:
                users = users.filter(
                    first_name=request_serializer.data['first_name']
                )
            if request_serializer.data['last_name']:
                users = users.filter(
                    last_name=request_serializer.data['last_name']
                )

            serializer = UsersSerializer(instance=users, many=True)
            return JsonResponse(
                {
                    'data': serializer.data
                }
            )
        else:
            return JsonResponse(
                request_serializer.errors,
                status=400
            )





    # if request.method == 'GET':
        # user_list=[]
        # users=User.objects
        # if 'first_name' in request.GET:
        #     users=users.filter(first_name=request.GET['first_name'])
        #
        # if 'last_name' in request.GET:
        #     users=users.filter(last_name=request.GET['last_name'])
        #
        # else:
        #     users=users.all()
        #
        # for u in users:
        #     user_list.append(
        #         {
        #             'first_name': u.first_name,
        #             'last_name' : u.last_name,
        #             'id'  : u.id,
        #         }
        #     )
        #
        # return JsonResponse(
        #     {
        #         "users" : user_list
        #     }
        # )
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.POST)

        if serializer.is_valid():
            user=serializer.save()


        else:
            # print(serializer)
            # print(dir(serializer))
            # print("Is Valid???",serializer.is_valid())

            # if serializer.is_valid() == True:

            # print("False")
            # print(serializer.errors)
            return JsonResponse(
                serializer.errors,status=400
            )
        # print(request.POST)
        # print(serializer.data)

        # u=User(
        #     first_name = serializer.data['first_name'],
        #     last_name = serializer.data['last_name]',
        #     birthday = birthday,
        #     number_of_friends=number_of_friends
        # )
        # u.save()

        return JsonResponse({
        "user" : {
            'first_name' : user.first_name,
            'last_name' : user.last_name,
            'id' : user.id
        }
    })



        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # birthday = request.POST['birthday']
        # number_of_friends = request.POST['number_of_friends']
        # print(len(first_name))
        # if len(first_name) > 20:
        #
        #     return JsonResponse(
        #         {
        #             'message' : 'First Name Max Length is 20'
        #         },
        #         status = 400
        #     )
        #
        # try:
        #     number_of_friends = int(number_of_friends)
        # except ValueError:
        #     return JsonResponse(
        #         {
        #             'message' : 'Number Of Friends is a IntegerField'
        #         },
        #         status = 400
        #     )
        # birthday = datetime.fromisoformat(birthday)
        #
        # print(type(number_of_friends))
#         u=User(
#             first_name = first_name,
#             last_name = last_name,
#             birthday = birthday,
#             number_of_friends=number_of_friends
#         )
#         u.save()
#
#         return JsonResponse(
#     {
#         "users" :{
#             'first_name': u.first_name,
#             'last_name' : u.last_name,
#             'id'  : u.id,
#         }
#     }
# )
