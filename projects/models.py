from django.db import models
import os
absolute_path = os.path.abspath(__file__)
dir_path = os.path.dirname(absolute_path) + "/static/images"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path=dir_path)

    # def __str__(self):
    #     return self.title
