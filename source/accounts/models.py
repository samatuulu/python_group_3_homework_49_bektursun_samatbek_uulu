from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserLink.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_link.save()