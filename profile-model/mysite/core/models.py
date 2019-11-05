from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError



def validate_image(image):
    file_size = image.file.size
    limit = 2
    if file_size > limit * 1024 *1024:
        raise ValidationError("Max size of file is %s MB" % limit)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', blank=True, null=True ,validators=[validate_image]) 


    def __str__(self):
    	return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
