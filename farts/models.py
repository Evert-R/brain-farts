from django.db import models
from tags.models import Categories, Types, Topics, Projects
from django.contrib.contenttypes.fields import GenericForeignKey


class Fart(models.Model):
    """
    Fart model
    """
    TYPE_CHOICES = [
        ('LINK', 'Link'),
        ('IMAGE', 'Image'),
        ('AUDIO', 'Audio'),
        ('TEXT', 'Text'),
    ]
    title = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=5,
                            choices=TYPE_CHOICES,
                            default='TEXT')
    topic = models.ForeignKey(
        Topics, on_delete=models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(
        Projects, on_delete=models.SET_NULL, blank=True, null=True)
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(blank=True, null=True,
                             upload_to="audio/%Y-%m-%d/%H-%M-%S")
    image = models.ImageField(blank=True, null=True,
                              upload_to='images/%Y-%m-%d/%H-%M-%S')
    link = models.CharField(blank=True, null=True, max_length=1000)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.text[0:100]
