from django.db import models

class PairRequest(models.Model):
    username = models.CharField(max_length=31)
    event = models.CharField(max_length=31, default="PyCon 2015")
    languages = models.CharField(max_length=1023, default="Python/Django")
    description = models.TextField()
    expires_in = models.DateTimeField()
