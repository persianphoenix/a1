from django.db import models

class Todo(models.Model):
    firstName=models.CharField(max_length=30),
    title=models.CharField(max_length=100),
    bodytext=models.TextField(),
    datecreated=models.DateField()