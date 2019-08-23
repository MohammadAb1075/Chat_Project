from django.db import models

from django.contrib.auth.models import User

# from users.models import User


class Conversation(models.Model):
    name     = models.CharField(max_length = 100)
    members  = models.ManyToManyField(User)
    is_group = models.BooleanField(null = True)

    def __str__(self):
        return self.name

# class ConversationMember(models.Model):
#     conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE)
#     user         = models.ForeignKey(User, on_delete = models.DO_NOTHING)
#
#     def __str__(self):
#         return "{} , {}".format(self.conversation,self.user)


class Message(models.Model):
    sender       = models.ForeignKey(User, on_delete = models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE)
    text         = models.TextField()
    date         = models.DateField(null = True)

    def __str__(self):
        return("{} ({}) : {} ".format(self.sender.first_name,self.conversation.name,self.text))
