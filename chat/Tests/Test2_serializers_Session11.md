from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from chat.models import Conversation,Message


class RequestChatSerializer(serializers.Serializer):

    text = serializers.CharField()
    conversation = serializers.IntegerField(min_value=1)

    def create(self, validated_data):

        c = Conversation.objects.get(
                id=validated_data['conversation'])
        m = Message(
            conversation = c,
            text = validated_data['text'],
            date = datetime.now(),
            sender=self.context['user']
            # sender = validated_data
        )
        m.save()
        return m
