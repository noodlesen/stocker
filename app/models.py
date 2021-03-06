from django.db import models

# Create your models here.

class Theme(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)

class Marketplace(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255, null=True, blank=True)

class Motion(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)


class Project(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    folder = models.CharField(max_length=50)
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL)


class Footage(models.Model):

    def __str__(self):
        return '%s (%s)' % (str(self.name),str(self.filename))

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    motion = models.ForeignKey(Motion, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    finished = models.BooleanField(default=False)
    rendered = models.BooleanField(default=False)
    filename = models.CharField(max_length=50, blank=True, null=True)
    resolution_x = models.IntegerField(default=4096)
    resolution_y = models.IntegerField(default=2304)
    has_alpha = models.BooleanField(default=False)
    keywords_raw = models.TextField(blank=True, null=True)


class Publication(models.Model):
    def __str__(self):
        return self.marketplace.name+': '+self.footage.name
    footage = models.ForeignKey(Footage, on_delete=models.CASCADE)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    link = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
