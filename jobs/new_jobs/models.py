from django.db import models
from django.contrib.auth.models import  User

class NewJob(models.Model):
    position_name = models.CharField(max_length=200)
    text_descriptoon = models.TextField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    salary = models.IntegerField()
    n_openings = models.IntegerField()
    creator  = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return self.position_name
