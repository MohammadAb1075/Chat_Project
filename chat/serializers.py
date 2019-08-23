from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from chat.models import Conversation,Message
from users.serializers import UserProfileSerializer,ShortUserProfileSerializer

class ConversationSerializer(serializers.ModelSerializer):

    members = ShortUserProfileSerializer(many = True)

    class Meta:
        model = Conversation
        fields = '__all__'



class RequestChatSerializer(serializers.Serializer):

    text         = serializers.CharField()
    conversation = serializers.IntegerField(min_value=1)

    def create(self, validated_data):

        c = Conversation.objects.get(
                id=validated_data['conversation'])
        m = Message(
            conversation = c,
            text = validated_data['text'],
            date = datetime.now(),
            sender = self.context['user']
            # sender = validated_data
        )
        m.save()
        return m

class ResponseMessageListSerializer(serializers.ModelSerializer):

    sender       = UserProfileSerializer()
    conversation = ConversationSerializer()

    class Meta:
        model = Message
        fields = '__all__'



class EditMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields =['id','text']

    def update(self,instance ,validated_data):
        instance.text  = validated_data['text']

        instance.save()
        return  instance


class AllMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class CreateConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'


    # def create(self, data):
    #     c = Conversation(
    #         name = data['name'],
    #         is_group   = data['is_group'],
    #
    #     )
    #     c.save()
    #     for i in data['members']:
    #         c.members.add(i)
    #     c.save()
    #
    #     return c
