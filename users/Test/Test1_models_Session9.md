from django.db import models



class User(models.Model):
    username          = models.CharField(max_length = 30)
    password          = models.CharField(max_length = 128)
    first_name        = models.CharField(max_length = 100)
    last_name         = models.CharField(max_length = 100)
    birthday          = models.DateField(null = True)
    number_of_friends = models.IntegerField()
    token             = models.CharField(null = True, max_length = 36)


    def __str__(self):
        return(self.first_name + " " + self.last_name)
