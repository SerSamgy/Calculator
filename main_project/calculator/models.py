from django.db import models

class Solver(models.Model):
    expression = models.CharField(max_length=20, blank=True, default='0')
    result = models.CharField(max_length=20, blank=True, default='0')
