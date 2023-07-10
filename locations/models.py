from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Village(models.Model):
    name = models.CharField(max_length=25)
    district = models.ForeignKey(to=District, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.district}'
    

class Stage(models.Model):
    name = models.CharField(max_length=25)
    village = models.ForeignKey(to=Village, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}, {self.village}'