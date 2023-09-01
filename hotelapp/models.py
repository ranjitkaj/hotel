from django.db import models



class register(models.Model):
    check_in = models.CharField(max_length=50)
    check_out = models.CharField(max_length=50)
    adults = models.CharField(max_length=50)
    childs = models.CharField(max_length=50)
    rooms = models.CharField(max_length=50)


class massege(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=15)
    msg = models.CharField(max_length=50)
    



# Create your models here.
