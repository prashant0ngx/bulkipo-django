from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DmatsAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=40)
    capital = models.IntegerField()
    username = models.IntegerField()
    password = models.CharField(max_length=100)
    crn = models.CharField(max_length=60)
    pin = models.IntegerField()
    def __str__(self):
        return self.name

class Share(models.Model):

    username = models.ForeignKey(DmatsAccount, on_delete=models.CASCADE)
    qty = models.IntegerField()
    def __int__(self):
        return self.username


    
