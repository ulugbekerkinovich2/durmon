from django.db import models


# Create your models here.
class Contact(models.Model):
    phone = models.BigIntegerField()

    def __str__(self):
        return f"raqam : {self.phone}"


class Boglanish(models.Model):
    name = models.CharField(max_length=300)
    phone = models.BigIntegerField()

    def __str__(self):
        return f" {self.name}, {self.phone}"
