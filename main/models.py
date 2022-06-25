from django.db import models

class t1(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)


class t2(models.Model):
    name = models.CharField(max_length=100)
    game_no = models.CharField(max_length=100)
    activity_1 = models.CharField(max_length=100)
    activity_2 = models.CharField(max_length=100)
    activity_3 = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    narrative = models.CharField(max_length=100)
    
