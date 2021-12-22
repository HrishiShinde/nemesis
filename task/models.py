import typing
from django.db import models

# Create your models here.
class User(models.Model):

    id = models.AutoField(primary_key= True)
    name = models.TextField(max_length= 50)
    email = models.TextField(max_length= 50)
    password = models.TextField(max_length= 50)
    address = models.TextField(max_length= 200)

    class Meta:
        db_table = "User"


