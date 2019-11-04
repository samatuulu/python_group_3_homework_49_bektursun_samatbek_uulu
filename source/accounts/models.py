from django.contrib.auth.models import User
from django.db import models


class UserLink(models.Model):
    user = models.OneToOneField(User, related_name='user_link', verbose_name='User', on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')
    about = models.TextField(max_length=1000, null=True, blank=True, verbose_name='About')
    link = models.URLField(max_length=200, verbose_name='Link', null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'