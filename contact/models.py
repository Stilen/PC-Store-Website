from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name
