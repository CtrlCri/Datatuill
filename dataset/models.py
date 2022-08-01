from django.db import models
from django.conf import settings

class Dataset(models.Model):
    title = models.CharField(max_length=80)
    slug_title = models.SlugField

    code = models.TextField(blank=False)
    about = models.TextField(blank=False)
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    num_downloads = models.IntegerField(default=0)

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Like(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dataset = models.ForeignKey(Dataset, related_name='likes', on_delete=models.CASCADE)

