from django.contrib import admin
from .models import UserLink
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserLinkInline(admin.StackedInline):
    model = UserLink
    fields = ['profile_photo', 'about', 'link']


class UserLinkAdmin(UserAdmin):
    inlines = [UserLinkInline]


admin.site.unregister(User)
admin.site.register(User, UserLinkAdmin)