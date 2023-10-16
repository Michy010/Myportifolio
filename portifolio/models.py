from django.db import models

# Create your models here.

class PortfolioProject (models.Model):
    title = models.CharField (max_length=100)
    description = models.TextField ()
    image = models.ImageField (upload_to= 'portfoilio_images/', null= True, blank=True)
    technologies_used = models.CharField (max_length=100)
    website_link = models.URLField (null=True, blank=True)

    def __str__(self):
        return self.title
