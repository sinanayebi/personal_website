from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project')

    def __str__(self):
        return self.title

