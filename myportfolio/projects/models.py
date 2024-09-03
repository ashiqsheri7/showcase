from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.name
