from django.db import models


# Create your models here.

class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    no = models.CharField(max_length=128, unique=True, primary_key=True)
    password = models.CharField(max_length=256)
    mail = models.EmailField(unique=True)
    sex = models.CharField(max_length=16, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.no

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
