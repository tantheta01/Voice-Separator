from django.db import models
from django.contrib.auth import User


class AppUser(models.Model):

	user = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username

# Create your models here.
