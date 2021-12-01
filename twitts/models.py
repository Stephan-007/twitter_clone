from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Twitt(models.Model):
    class Meta(object):
        db_table = 'tweet'
    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default=''
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    date = models.DateTimeField(
        'Created time', blank=True, auto_now=True
    )
    image = CloudinaryField('image', blank=True
                            )
    likes = models.PositiveBigIntegerField(
        'like', default=0, blank=True, db_index=True
    )
