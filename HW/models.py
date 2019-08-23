# from django.db import models

# class User(models.Model):
#     first_name        = models.CharField(max_length = 100)
#     last_name         = models.CharField(max_length = 100)
#     birthday          = models.DateField(null=True)
#     number_of_friends = models.IntegerField()

#     def __str__(self):
#         return(self.first_name + " " + self.last_name)


# class Message(models.Model):
#     sender    = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blahblah")
#     receiver  = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blahblah2")
#     text      = models.TextField()
#     date      = models.DateField()

#     def __str__(self):
#         return("{} -> {} : {}".format(self.sender,self.receiver,self.text))

    
