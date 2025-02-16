
# Create your models here.



from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    mp3_file = models.FileField(upload_to='uploads/mp3s/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
