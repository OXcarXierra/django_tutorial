from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='projects/', null=False)
    created_at = models.DateField(auto_created=True, null=True)
