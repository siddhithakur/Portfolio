from django.db import models

class Blogs(models.Model):
    blog=models.CharField(max_length=100)
    about=models.CharField(max_length=1000)
    url=models.URLField(blank=True)
    
