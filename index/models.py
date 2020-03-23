from django.db import models

class TimeModel(models.Model):
    time =  models.DateTimeField(blank = True  , null = True)
    tmp_min =  models.FloatField(blank = True  , null = True)
    tmp_max =  models.FloatField(blank = True  , null = True)
    tmp_c = models.FloatField(blank = True , null = True)
    humidity = models.IntegerField(blank = True , null = True)
    status = models.CharField(max_length = 12)
    icon_url = models.CharField(max_length = 50)
