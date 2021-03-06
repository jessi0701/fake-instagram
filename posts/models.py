from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=100)
    #image = models.ImageField(blank=True)
    
                
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
                upload_to='posts/images',
                processors=[ResizeToFill(600,600)],
                format='JPEG',
                options={'quality':90},
                )