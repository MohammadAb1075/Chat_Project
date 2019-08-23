from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
class ChatView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    @method_decorator(login_required)
    def post(self,request):
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
