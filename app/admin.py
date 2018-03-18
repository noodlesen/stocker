from django.contrib import admin
from .models import Project,Footage, Motion, Marketplace, Publication, Theme

# Register your models here.

#class ProjectAdmin(admin.ModelAdmin):

admin.site.register(Project)
admin.site.register(Footage)
admin.site.register(Motion)
admin.site.register(Marketplace)
admin.site.register(Publication)
admin.site.register(Theme)