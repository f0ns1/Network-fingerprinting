from datetime import date

from django.db import models

class DefaultModule(models.Model):
    operation = models.CharField(max_length=60)
    target_ip = models.CharField(max_length=60, default=None)
    target_port = models.IntegerField(default=-1)
    local_ip = models.CharField(max_length=60, default="127.0.0.1")
    local_port = models.IntegerField(default=4444)
    output = models.CharField(max_length=5000, default="None")
    time = models.DateTimeField(max_length=60, default= date.today())
    def __str__(self):
        return self.name


