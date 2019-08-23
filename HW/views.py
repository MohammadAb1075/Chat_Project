# from datetime import datetime

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.utils.datastructures import MultiValueDictKeyError

# from HW.models import User , Message

# def user_list(request):
#     if request.method == 'GET':
#         try:
#             query = request.GET["search"]
#             users = User.objects.filter(first_name=query)
#         except MultiValueDictKeyError:
#             users = User.objects.all()
#         messages=Message.objects.all()
#         return render(
#             request,
#             "List.html",
#             {
#                 "users"    : users,
#                 "messages" : messages
#             }
#         )
#     elif request.method == 'POST':
#         try:
#             u=User(
#             first_name=request.POST['firstname'],
#             last_name=request.POST['lastname'],
#             number_of_friends=12,
#             )

#             u.save()
#             users = User.objects.all()
#         except:


#             #
#             # for u in User.objects.all():
#             #     if u.first_name == request.POST['sendername']:
#             #         s=request.POST['sendername']
#             s=''
#             r=''
#             for u in User.objects.all():
#                 if u.first_name == request.POST['sendername']:
#                     s=request.POST['sendername']
#                     for u1 in User.objects.all():
#                         if u1.first_name == request.POST['receivername']:
#                             r=request.POST['receivername']

#                             m=Message(
#                             sender=u,
#                             receiver=u1,
#                             text=request.POST['Text'],
#                             date=datetime.now()
#                             ).save()
#                             messages=Message.objects.all()

#                         else:
#                             pass
#             else:
#                 pass
#         users = User.objects.all()
#         messages = Message.objects.all()

#         return render(

#             request,
#             "List.html",
#             {
#                 "users" : users,
#                 "messages" : messages

#             }
#         )
