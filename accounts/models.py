from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.dispatch import receiver

@receiver(user_registered)
def on_user_registered(sender, **kwargs):
    """Handle user registration to create a profile"""
    request = kwargs['request']
    user = kwargs['user']
    profile = Profile(
        user=user,
        department=request.POST['department'],
        student_id=request.POST['student_id'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name']
    )
    profile.save()

class Profile(models.Model):
    """Extra fields for user model"""
    user = models.OneToOneField(User)

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    student_id = models.CharField(max_length=120)
