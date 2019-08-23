import hashlib
# from users.models import User
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime


class RequestSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, data):
        u = User(
            first_name = data['first_name'],
            last_name  = data['last_name'],
            username   = data['username'],
        )
        u.set_password(data['password'])
        u.save()
        return u

class RequestLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, allow_blank=False, max_length=30)
    password = serializers.CharField(
        required=True, allow_blank=False, max_length=128)


class RequestGetSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=False, allow_blank=False, max_length=100)

    def validate(self, data):
        if 'first_name' not in data and 'last_name' not in data:
            raise serializers.ValidationError(
                'At least one of firstname or lastname parameters are required'
            )
        return data




class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=True, allow_blank=False, max_length=100)
    last_name = serializers.CharField(
        required=True, allow_blank=False, max_length=100)
    birthday = serializers.DateField()
    number_of_friends = serializers.IntegerField(
        default=10, min_value=0)


    # def validate_number_of_friends(self, data):
    #     if data == 5:
    #         raise serializers.ValidationError(
    #             'In this Country, You cant have 5 friends!!!'
    # )
    #     return data

    def to_integer(self,dt_time):
        y=dt_time.year
        return y

    def validate(self,data):
        if  self.to_integer(datetime.now()) - self.to_integer(data['birthday']) < 18 :

            if data['number_of_friends'] > 5 :
                raise serializers.ValidationError(
                    'In this Country, You cant  have more than 5 friends!!!'
                )
        if data["number_of_friends"] == 5:
            raise serializers.ValidationError(
                'In this Country, You cant have 5 friends!!!')
        return data

    def create(self ,validated_data):
        print("I'm in the Create Function")
        u = User(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            birthday = validated_data['birthday'],
            number_of_friends = validated_data['number_of_friends']
        )
        u.save()
        return u
