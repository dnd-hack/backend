from django.contrib import admin

# Register your models here.
from accounts.models import User
from match.models import Group, JoinedMember


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass

@admin.register(JoinedMember)
class JoinedMemberAdmin(admin.ModelAdmin):
    pass