from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# from users.models import User
from chat.models import Conversation , Message


def conversation_view(request,id):
    print(type(id))
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        try:
            print(request.POST["message"])
            u3=User.objects.all()[3]
            Message(
                sender=u3,
                conversation=Conversation.objects.filter(id=int(id))[0],
                text=request.POST["message"],
                date=datetime.now()
            ).save()
        except:
            print("There is no userparameter")

    try:
        messages=Message.objects.filter(conversation=int(id))

    except:
        messages=[]

    return render(
        request,
        "Conversationlist7.html",
        {
            "messages"     : messages,
            "conversation" : Conversation.objects.all(),
        }
    )
