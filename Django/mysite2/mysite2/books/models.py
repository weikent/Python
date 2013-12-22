from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 60)
    state_province = models.CharField(max_length = 30)
    country = models.CharField(max_length = 50)
    website = models.URLField()
    
    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    second_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.second_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

    
class test(models.Model):
    test1 = models.CharField(max_length = 20)
#    test2 = models.datetime()
    test2 = models.DateField()


# Create your models here.
