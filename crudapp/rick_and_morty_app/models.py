from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.TextField()
    lastEpisode = models.TextField()
    images = models.FileField(upload_to='images/')

    # this method is so that the character name appears in django admin
    def __str__(self):
        return self.name