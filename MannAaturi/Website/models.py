from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Video(models.Model):
    Video = EmbedVideoField()  
    Title = models.CharField(max_length=100, default="")
    Description = models.TextField(max_length=500, default="")

    def __str__(self) -> str:
        return self.Title

class Message(models.Model):
    Email = models.EmailField(default="")
    Username = models.CharField(max_length=100, default="")
    First_Name = models.CharField(max_length=150, default="")
    Last_Name = models.CharField(max_length=150, default="")
    Message = models.TextField(max_length=1000, default="")

    def __str__(self) -> str:
        return "Message from " + self.First_Name + " " + self.Last_Name

class Pdf(models.Model):
    Title = models.CharField(max_length=100)
    File = models.FileField(upload_to="")

    def __str__(self) -> str:
        return self.Title