from django.contrib import admin

# Register your models here.
from accounts.models import User
from match.models import Group


@admin.register(Group)
class ProfileAdmin(admin.ModelAdmin):
    pass