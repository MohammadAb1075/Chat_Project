from datetime import datetime

from django.shortcuts import render

from users.models import User
from chat.models import Conversation , Message

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.serializers import RequestChatSerializer


class ChatView(APIView):
    def post(self,request):
        serializer = RequestChatSerializer(data=request.data)
        if serializer.is_valid():
            # try:
            #     User.objects.get(token=serializer.date['token'])
            # except:
            #     return Response(
            #         {
            #             'message' : 'token is Wrong !'
            #         },
            #         status=status.HTTP_403_FORBIDEN
            #     )

            u,s = serializer.save()
            if s == 403:
                return Response(
                    {
                        'message' : 'token or conversation is Wrong !'
                    },
                    status=status.HTTP_403_FORBIDDEN
                )

            return Response(
                {
                    'Message' : 'Message Saved'
                }
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
