from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100),
    email = models.EmailField,
    is_admin = models.BooleanField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=200),
    author = models.ForeignKey('User', on_delete=models.CASCADE),
    created_at = DateField.auto_now_add,
    # TODO: figure out file upload directory
    file = models.FileField

class Contact(models.Model):
    email = models.EmailField,
    linkedin = models.URLField
