from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from djangochat.utils import CsrfExemptSessionAuthentication
from django.contrib.auth.models import AnonymousUser
# from chat.models import Conversation , Message
from chat.serializers import RequestChatSerializer

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
                    'salam' : 123
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
