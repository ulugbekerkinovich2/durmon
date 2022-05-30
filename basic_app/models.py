from django.db import models


# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.phone


class Boglanish(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)

    def __int__(self):
        return f" {self.name}, {self.phone}"
