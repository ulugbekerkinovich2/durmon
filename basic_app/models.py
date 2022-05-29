from django.db import models


# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=27)

    def __str__(self):
        return f"telefon raqami  {self.phone}"
