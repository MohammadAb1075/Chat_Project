from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from djangochat.utils import CsrfExemptSessionAuthentication
from django.contrib.auth.models import AnonymousUser
from chat.models import Conversation , Message
from chat.serializers import *

 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ChatView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        if type(request.user) is AnonymousUser:
            return Response(
                {
                    'message' : 'UnAuthorize !!!'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        else:
            serializer = RequestChatSerializer(
                data=request.data,
                context={
                    'user'  : request.user,
                    # 'salam' : 123
                }
            )

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

    def put(self, request):
        message=Message.objects.get(id = request.data['id'])
        serializer = EditMessageSerializer(instance=message,data=request.data )
        if serializer.is_valid():
            serializer.save()

            return Response({
                'message': 'Edited successfuly',
                'data': serializer.data
            })
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def get(self, request):
        messages = Message.objects.filter(conversation = request.GET['conversation']).all()

        serializer = AllMessageSerializers(messages, many=True)
        return Response(
            {
                'data' : serializer.data
            },
            status=status.HTTP_200_OK
        )





class MessageListView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    @method_decorator(login_required)
    def get(self, request):
        messages = Message.objects.all()
        serializer = ResponseMessageListSerializer(messages, many=True)
        serializer.save()
        return Response(
            {
                'data' : serializer.data
            },
            status=status.HTTP_200_OK
        )




class ConversationList(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request):
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many = True)
        return Response(
            {
                'data' : serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = CreateConversationSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message' : 'Conversation Create'
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'message' : 'Error'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
