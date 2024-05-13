from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models

# Create your models here.


class Urls(models.Model):
    url = models.URLField()
    uuid = models.CharField(max_length=255,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created and not instance.is_superuser and not instance.is_staff:
        Token.objects.create(user=instance)