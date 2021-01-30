from django.db import models

# Create your models here.

class Form(models.Model):
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.email + ' ' + self.subject + ' ' + self.description
