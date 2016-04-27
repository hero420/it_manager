from django.contrib import admin
from cmdb import models
# Register your models here.
class User_Info(admin.ModelAdmin):
    pass
admin.site.register(models.User_Info,User_Info)