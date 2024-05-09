from django.db import models

# Create your models here.


class Urls(models.Model):
    url = models.URLField()
    uuid = models.CharField(max_length=255,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)