from django.db import models
from locations.models import Stage


# Create your models here.


class Member(models.Model):
    REQUIRED_FIELDS = ['first_name', 'last_name']
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(verbose_name='Member email', blank=True)
    title = models.CharField(max_length=25)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=1, default="O")
    display_picture = models.ImageField(
        default='display_pictures/smily.jpg', upload_to='display_pictures')
    village = models.CharField(max_length=25)
    stage = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)
    card_id = models.IntegerField(
        unique=True, verbose_name="Membership card id")
    issue_date = models.DateTimeField(verbose_name="Date of issue of card")
    expiry_date = models.DateTimeField(verbose_name="Date of expiry of card")

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
