from django.db import models

class Solver(models.Model):
    cur_val = models.IntegerField(default=0)
    res_val = models.IntegerField(default=0)
    sign = models.CharField(max_length=1, blank=True, default=None)
    result = models.CharField(max_length=10, blank=True, default='0')
