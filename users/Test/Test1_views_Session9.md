import random
import uuid
from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from users.serializers import *


class CsrfExemtSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self,request):
        return


class SignupView(APIView):

    def post(self, request):
        serializer = RequestSignupSerializer(data=request.data)
        if serializer.is_valid():
            u = serializer.save()
            print(u)
            return Response({
                'message': 'your account have been created successfuly',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginView(APIView):
    authentication_classes = (CsrfExemtSessionAuthentication, BasicAuthentication)
    def post(self, request):
        serializer = RequestLoginSerializer(data=request.data)
        if serializer.is_valid():

            u = authenticate(
                request,
                username=serializer.data['username'],
                password=serializer.data['password'])

            if u is None:
                return Response(
                    {
                        'message': 'There is not any account with this username'
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            # if u.check_password(serializer.data['password']):
        #         print(u)
        #         print(login(request, u))
            login(request, u)
            return Response(
                {
                    'message': 'Your account info is correct',
                    'data': {
                        'first_name': u.first_name,
                        "id": u.id,
                    }
                },
                status=status.HTTP_200_OK
            )
           # if u:
           #      print(u, request)
           #      login(request, u)
           #      return JsonResponse(
           #          {
           #              'message': 'Your account info is correct',
           #              'data': {
           #                  'first_name': u.first_name,
           #                  "id": u.id,
           #              }
           #          },
           #          status=status.HTTP_200_OK
           #      )


class EditProfile(APIView):
    authentication_classes = (CsrfExemtSessionAuthentication, BasicAuthentication)
    def put(self,request):

        serializer = EditProfileSerializer(data=request.data)

        if serializer.is_valid():

            serializer.update(request.user,request.data)

            return Response({
                'message': 'your account have been Edited successfuly',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserListItemView(APIView):

    def get(self, request):
        request_serializer = RequestGetSerializer(data=request.GET)
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

            return Response(
                {
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                request_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response(
            {
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
