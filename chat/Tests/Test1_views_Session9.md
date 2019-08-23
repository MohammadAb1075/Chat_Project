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
            serializer.save()
            return Response(
                {
                    'Message' : 'Message Saved'
                }
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
