from django.db import models

# Create your models here.
"""
    class Post:
    tittle: str
    author: str
    content: str
    thumbnail: img
"""

class Post(models.Model):
    tittle = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', default='default.png')
    date_created = models.DateTimeField(auto_now_add=True)
    
   
    def __str__(self):
        # return self.tittle
        return f"<Post {self.tittle}>"
    


