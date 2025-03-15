from django.db import models

# Create your models here.


class UplaodedImage(models.Model):
    image = models.ImageField(upload_to='uploads')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f'image {self.id}')