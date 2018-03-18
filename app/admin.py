from django.contrib import admin
from .models import Project,Footage, Motion, MarketPlace

# Register your models here.

#class ProjectAdmin(admin.ModelAdmin):

admin.site.register(Project)
admin.site.register(Footage)
admin.site.register(Motion)
admin.site.register(MarketPlace)