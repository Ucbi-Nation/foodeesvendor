from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=False, default=0)
    last_name = models.CharField(max_length=20, null=False, default=0)
    username = models.CharField(max_length=20, null=False, default=0)
    phone_number = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    email = models.EmailField(null=True)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')
    income = models.IntegerField(null=False, default=0)
    orders = models.IntegerField(null=False, default=0)
    visitor = models.IntegerField(null=False, default=0)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    auth = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

