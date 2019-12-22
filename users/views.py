import random
import uuid
import hashlib
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
# from django.core import mail

from django.core.mail import send_mail, BadHeaderError

 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangochat.utils import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from users.serializers import *


class SignUpView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        serializer = RequestSignUpSerializer(data=request.data)
        if serializer.is_valid():
            u=serializer.save()
            print(u)
            # send_mail('subject', 'hiiiiiiiiiiiiiiiiii', 'mabdollah1375@gmail.com',['persianrobo4@gmail.com']) #list(request.data['email']))
            # print(mail)
            return Response(
                {
                    'Message' : 'Account Create',
                    'data'  : serializer.data
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        serializer = RequestLoginSerializer(data=request.data)
        if serializer.is_valid():

            user = authenticate(
            request,
            username=serializer.data['username'],
            password=serializer.data['password']
            )

            if user is None:
                return Response(
                    {
                        'Message' : 'There is No Any Account With This Username !!!',
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            if user:
                login(request,user)
                return Response(
                    {
                        'message': 'Your account info is correct',
                        'data':
                        {
                            'first_name': user.first_name,
                            "id": user.id,
                        }
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                    'message' : 'Your Password is Wrong !!!'
                    }
                )

        else:
            return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
            )


class EditProfileView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def put(self,request):

        # serializer = EditProfileSerializer(instance=request.user,data=request.data)
        serializer = EditProfileSerializer(data=request.data)

        if serializer.is_valid():

            serializer.update(request.user,request.data)
            # serializer.save()
            return Response({
                'message': 'your account have been Edited successfuly',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserListItemView(APIView):

    def get(self,request):
        try:
            request_serializer = RequestGetSerializer(data=request.GET) #data=request.data
            if request_serializer.is_valid():
                users = User.objects
                if 'first_name' in request_serializer.data:
                    users = users.filter(
                        first_name=request_serializer.data['first_name']
                    )
                if 'last_name' in request_serializer.data:
                    users = users.filter(
                        last_name=request_serializer.data['last_name']
                    )
                serializer=UserSerializer(instance=users,many=True)
                return Response(
                    {
                        "users" : serializer.data
                    },
                    status=status.HTTP_200_OK
                )

            else:
                return Response(
                    request_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            users = User.objects.all()
            serializer = ResponseUserListSerializer(users, many = True)
            return Response(
                {
                    'data' : serializer.data
                },
                status=status.HTTP_200_OK
            )

    def post(self,request):
        serializer = UserSerializer(data=request.POST)#data=request.data

        if serializer.is_valid():
            serializer.save()

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
            "user" : serializer.data
            },
            status=status.HTTP_201_CREATED
        )



class UserListView(APIView):
    def get(self, requeest):
        users = User.objects.all()
        serializer = ResponseUserListSerializer(users, many = True)
        return Response(
            {
                'data' : serializer.data
            },
            status=status.HTTP_200_OK
        )
