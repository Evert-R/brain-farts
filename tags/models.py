from django.db import models


class Types(models.Model):
    """
    tags: type
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
       ordering = ['name',]


class Projects(models.Model):
    """
    tags: project
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
       ordering = ['name',]


class Categories(models.Model):
    """
    tags: category
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
       ordering = ['name',]


class Topics(models.Model):
    """
    tags: topic
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
       ordering = ['name',]
