from django.db import models

# Create your models here.


class Footer(models.Model):
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=60)
    whatsapp = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)


class SendMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.name} -- {self.email}'
