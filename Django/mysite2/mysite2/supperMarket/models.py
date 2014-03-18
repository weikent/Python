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


class ImagePath(models.Model):
    """
    """
    name = models.CharField(max_length = 30)
    image1 = models.CharField(max_length = 500)
    image2 = models.CharField(max_length = 500)
    image3 = models.CharField(max_length = 500)
    image4 = models.CharField(max_length = 500)
    image5 = models.CharField(max_length = 500)
    image6 = models.CharField(max_length = 500)
    image7 = models.CharField(max_length = 500)
    image8 = models.CharField(max_length = 500)
    image9 = models.CharField(max_length = 500)
    image10 = models.CharField(max_length = 500)
    image11 = models.CharField(max_length = 500)
    image12 = models.CharField(max_length = 500)
    image13 = models.CharField(max_length = 500)
    image14 = models.CharField(max_length = 500)
    image15 = models.CharField(max_length = 500)

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
