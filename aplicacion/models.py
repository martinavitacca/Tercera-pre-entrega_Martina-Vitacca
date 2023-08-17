from django.db import models

# Create your models here.

class Adventure(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)

class Puzzle(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)

class Retro(models.Model):
    title = models.CharField(max_length=50)
    developer = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    mode = models.CharField(max_length=100)

class RPGHorror(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)

class Stealth(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)

class Survival(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    mode = models.CharField(max_length=100)

class Player(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()