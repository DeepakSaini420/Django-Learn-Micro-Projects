from django.db import models
 
# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=225)
    salary = models.IntegerField()
    isActive = models.BooleanField(default=False)