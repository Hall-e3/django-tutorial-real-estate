# SIGNALS
# signals allow certain senders to notify receivers that certain actions have taken place
# users profile is created whenever the user object is created

 
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

# instance of a logger
logger = logging.getLogger(__name__)

@receiver(post_save,sender=AUTH_USER_MODEL)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=AUTH_USER_MODEL)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")