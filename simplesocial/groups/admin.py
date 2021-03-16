from django.contrib import admin
from . import models
# Register your models here.


#TabularInline makes the parent and child to edit at same page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
#no need for groupmember to register


admin.site.register(models.Group)
