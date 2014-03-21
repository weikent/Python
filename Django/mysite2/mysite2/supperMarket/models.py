from django.db import models

class MainSort(models.Model):
    name = models.CharField(max_length = 30)
    sortby = models.IntegerField()
    linkURL = models.CharField(max_length = 500)
    image = models.CharField(max_length = 500)
    onClick = models.CharField(max_length = 100, blank=True, null=True)
    devId = models.CharField(max_length = 20, blank=True, null=True)
    devClass = models.CharField(max_length = 20, blank=True, null=True )


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


class ImagePath(models.Model):
    """
    """
    name = models.CharField(max_length = 30)
    mainSort = models.ForeignKey(MainSort)
    sortby = models.IntegerField()
    image1 = models.CharField(max_length = 500, blank=True, null=True)
    image2 = models.CharField(max_length = 500, blank=True, null=True)
    image3 = models.CharField(max_length = 500, blank=True, null=True)
    image4 = models.CharField(max_length = 500, blank=True, null=True)
    image5 = models.CharField(max_length = 500, blank=True, null=True)
    image6 = models.CharField(max_length = 500, blank=True, null=True)
    image7 = models.CharField(max_length = 500, blank=True, null=True)
    image8 = models.CharField(max_length = 500, blank=True, null=True)
    image9 = models.CharField(max_length = 500, blank=True, null=True)
    image10 = models.CharField(max_length = 500, blank=True, null=True)
    image11 = models.CharField(max_length = 500, blank=True, null=True)
    image12 = models.CharField(max_length = 500, blank=True, null=True)
    image13 = models.CharField(max_length = 500, blank=True, null=True)
    image14 = models.CharField(max_length = 500, blank=True, null=True)
    image15 = models.CharField(max_length = 500, blank=True, null=True)
    link1 = models.CharField(max_length = 500, blank=True, null=True)
    link2 = models.CharField(max_length = 500, blank=True, null=True)
    link3 = models.CharField(max_length = 500, blank=True, null=True)
    link4 = models.CharField(max_length = 500, blank=True, null=True)
    link5 = models.CharField(max_length = 500, blank=True, null=True)
    link6 = models.CharField(max_length = 500, blank=True, null=True)
    link7 = models.CharField(max_length = 500, blank=True, null=True)
    link8 = models.CharField(max_length = 500, blank=True, null=True)
    link9 = models.CharField(max_length = 500, blank=True, null=True)
    link10 = models.CharField(max_length = 500, blank=True, null=True)
    link11 = models.CharField(max_length = 500, blank=True, null=True)
    link12 = models.CharField(max_length = 500, blank=True, null=True)
    link13 = models.CharField(max_length = 500, blank=True, null=True)
    link14 = models.CharField(max_length = 500, blank=True, null=True)
    link15 = models.CharField(max_length = 500, blank=True, null=True)

    def __unicode__(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.name


class Brand(models.Model):
    """
    """
    name = models.CharField(max_length = 30)
    sort = models.ForeignKey(SubSort)

    def __unicode__(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.name

class Kind(models.Model):
    """
    """
    name = models.CharField(max_length = 30)
    sort = models.ForeignKey(SubSort)

    def __unicode__(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.name

class Item(models.Model):
    """
    """
    name = models.CharField(max_length = 100)
    marketPrice = models.IntegerField()
    shorPrice = models.IntegerField()
    imagePath = models.CharField(max_length = 500)
    number = models.CharField(max_length = 20)
    stock = models.IntegerField()
    description = models.CharField(max_length = 2000)
    brand = models.ForeignKey(Brand)
    kind = models.ForeignKey(Kind)
    sort = models.ForeignKey(SubSort)
    def __unicode__(self):
        """
        
        Arguments:
        - `self`:
        """
        return self.name


# class Commentary(models.Model):
#     """
#     """

#     content = models.CharField(max_length = 500)
#     member = 
        

    
    


# Create your models here.
