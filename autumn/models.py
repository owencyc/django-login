from django.db import models


# Create your models here.
class Intro(models.Model):
    user_no = models.CharField(max_length=128, unique=True, primary_key=True)
    name = models.CharField(max_length=256)
    work = models.CharField(max_length=256)
    word = models.TextField()
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    p_word = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_no


class Skill(models.Model):
    user_no = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    score = models.IntegerField(default=90)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_no+self.name


class Verse(models.Model):
    user_no = models.CharField(max_length=128)
    content = models.TextField()
    author = models.CharField(max_length=128)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_no+self.author
