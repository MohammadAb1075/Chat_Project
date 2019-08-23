from datetime import datetime
from rest_framework import serializers
from chat.models import Conversation,Message
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist


class RequestChatSerializer(serializers.Serializer):

    text = serializers.CharField()
    conversation = serializers.IntegerField(min_value=1)


    def create(self, validated_data):
        # u = User.objects.get(
        #         token=validated_data['token'])
        c = Conversation.objects.get(
                id=validated_data['conversation'])
        m = Message(
            conversation=c,
            text=validated_data['text'],
            date='2019-08-10',
            sender=u
        )
        m.save()
        return m


    # def validate(self,data):
    #     '''
    #     check username & password is Correct
    #     '''
    #     try:
    #
    #         )
    #         u = User.objects.get(
    #             username = data['username'],
    #             password = data['password']
    #         )
    #     except ObjectDoesNotExist:
    #         raise serializers.ValidataionError(
    #             'Error'
    #         )
    #     return data



    # def create(self, validated_data):
    #     u = User.objects.get(username = validated_data['username'])
    #     c = Conversation.objects.get(id=validated_data['conversation'])
    #     m = Message(
    #         conversation=c,
    #         text=validated_data['text'],
    #         date='2019-11-01',
    #         sender=u
    #     )
    #     m.save()
    #     return m
