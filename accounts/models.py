from django.db import models
from django.contrib.auth.models import AbstractUser
from locations.models import Stage


# Create your models here.


class User(AbstractUser):
    REQUIRED_FIELDS = ['first_name', 'last_name']
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(verbose_name='User email', blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=1, default="O")
    display_picture = models.ImageField(
        default='display_pictures/smily.jpg', upload_to='display_pictures')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Member(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stage = models.ForeignKey(to=Stage, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25)
    card_id = models.IntegerField(
        unique=True, verbose_name="Membership card id")
    issue_date = models.DateTimeField(verbose_name="Date of issue of card")
    expiry_date = models.DateTimeField(verbose_name="Date of expiry of card")

    def __str__(self):
        return f'{self.user}'
