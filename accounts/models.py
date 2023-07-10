from django.db import models
from django.contrib.auth.models import AbstractUser
from locations.models import Stage

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.username}'
    

class Member(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    card_id = models.IntegerField()
    stage = models.ForeignKey(to=Stage, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25)