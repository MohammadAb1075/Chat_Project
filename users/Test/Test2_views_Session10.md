import random
import uuid
import hashlib
from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangochat.utils import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from users.serializers import RequestLoginSerializer, RequestGetSerializer, UserSerializer, RequestSignUpSerializer

def user_list_view(request):
    users = User.objects.all()
    return render(
        request,
        "userlist7.html",
        {
            "users" : users
        }
    )


class SignUpView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        serializer = RequestSignUpSerializer(data=request.data)
        if serializer.is_valid():
            u=serializer.save()
            print(u)
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
            # try:
            #     u=User.objects.get(username=serializer.data['username'])
            #
            # except ObjectDoesNotExist:
            #     return Response(
            #         {
            #             'Message' : 'There is not any account with this Username',
            #         },
            #         status=status.HTTP_404_NOT_FOUND
            #     )

            user = authenticate(
            request,
            username=serializer.data['username'],
            password=serializer.data['password']
            )
            # if user.password is None :
            #     return Response(
            #         {
            #             'Message' : 'Your password is Wrong'
            #         },
            #         status=status.HTTP_404_NOT_FOUND
            #     )
            #
            if user is None:
                return Response(
                    {
                        'Message' : 'Username or Password is Wrong !!!',
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            return Response(
                {
                    'Message'   : 'Your Account Info is Correct',
                    'data' :
                    {
                        'first_name' : user.first_name,
                        'id' : user.id,
                    }
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
             serializer.errors,
             status=status.HTTP_400_BAD_REQUEST
            )




class UserListItemView(APIView):

    def get(self,request):
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

    def post(self,request):
        serializer = UserSerializer(data=request.POST)#data=request.data

        if serializer.is_valid():
            serializer.save()

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_404_NOT_FOUND
            )

        return Response({
            "user" : serializer.data
            },
            status=status.HTTP_201_CREATED
        )
