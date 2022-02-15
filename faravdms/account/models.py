from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ADMINISTRATOR = 1
    READ = 2
    WRITE = 3
    
    ROLE_CHOICES = (
          (ADMINISTRATOR, 'Administrator'),
          (READ, 'Read'),
          (WRITE, 'Write'),
      )
    # gender = models.BooleanField(default=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    # You can create Role model separately and add ManyToMany if user has more than one role
      
