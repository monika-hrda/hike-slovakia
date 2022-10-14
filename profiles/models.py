from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

numeric = RegexValidator(r'^[0-9]', 'Only numbers are allowed!.')


class UserProfile(models.Model):
    """
    A user profile model for maintaining user details & booking history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True, validators=[numeric])

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
