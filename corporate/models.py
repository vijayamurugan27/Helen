from django.db import models

# Create your models here.


class Colleges(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField(blank = True, null = True)
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

class TechnicalTraining(models.Model):
    name = models.ForeignKey(Colleges, on_delete = models.CASCADE)
    dates = models.DateField(null = True, blank = True)
    First_year = models.BooleanField(default = False)
    Second_year = models.BooleanField(default = False)
    Third_year = models.BooleanField(default = False)
    Fourth_year = models.BooleanField(default = False)
    Rates = models.IntegerField(default = 1000)
    
