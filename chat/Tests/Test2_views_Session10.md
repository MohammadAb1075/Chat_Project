from datetime import datetime
from chat.models import Conversation , Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangochat.utils import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication
from chat.serializers import RequestChatSerializer

class ChatView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self,request):
        print('**********************',request.user)
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
