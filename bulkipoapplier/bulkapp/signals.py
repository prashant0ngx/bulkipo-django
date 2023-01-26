from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DmatsAccount, ApplyShare



@receiver(post_save, sender=DmatsAccount)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ApplyShare.objects.create(username=instance)

@receiver(post_save, sender=DmatsAccount)
def save_user_profile(sender, instance, **kwargs):
    instance.applyshare.save()



