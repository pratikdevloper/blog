from django.db import models

# Create your models here.
class Post(models.Model):
    objects = None
    title=models.CharField(max_length=150)
    desc=models.TextField()


    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=150)
    message=models.CharField(max_length=50)

    def __str__(self):
        return self.name