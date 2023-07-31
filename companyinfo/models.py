from django.db import models

# Create your models here.


class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=25)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logo/', blank=True, null=True)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    other_contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # image = models.ImageField(upload_to='services_image/', blank=True, null=True)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
