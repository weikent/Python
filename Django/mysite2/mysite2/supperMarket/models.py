from django.db import models

class MainSort(models.Model):
    name = models.CharField(max_length = 30)
    sortby = models.IntegerField()
    linkURL = models.CharField(max_length = 500)
    image = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.name


class SubSort(models.Model):
    """
    """
    
    name = models.CharField(max_length = 30)
    mainSort = models.ForeignKey(MainSort)
    sortby = models.IntegerField()
    def __unicode__(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.name


# Create your models here.
