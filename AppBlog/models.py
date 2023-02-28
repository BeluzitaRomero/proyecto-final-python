from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Post(models.Model):
    post_img = models.CharField(max_length= 250)
    post_description = models.CharField(max_length=200)
    username = models.CharField(max_length=40)

class Comment(models.Model):
    username = models.CharField(max_length=40)
    comment = models.CharField(max_length=200)