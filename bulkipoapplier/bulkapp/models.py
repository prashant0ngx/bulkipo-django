from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.


class DmatsAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    capital = models.IntegerField()
    username = models.IntegerField(
   
        unique=True,
        error_messages={
            'unique': ("A user with that db id already exists."),
        }
    )
    password = models.CharField(max_length=100)
    crn = models.CharField(max_length=200
    )
    pin = models.IntegerField()
    def __str__(self):
        return self.name

class Share(models.Model):
    username = models.ForeignKey(DmatsAccount,
        on_delete=models.CASCADE,
        null=False,
    )
    
    qty = models.IntegerField(
        null=False,
        validators=[MinValueValidator(10), MaxValueValidator(10000)],
    )
    
    def __int__(self):
        return self.username


    
