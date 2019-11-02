from django.db import models

# Create your models here.


class Spam(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    birthday = models.DateField(auto_now=False)
    email = models.EmailField(max_length=204)

    def __str__(self):
        return self.first_name
