from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserModels(models.Model):
    GENDER_CHOICES = [('Male', 'M'), ('Female', 'F')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length= 200, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')
    birth_date = models.DateField(auto_now_add=False)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
