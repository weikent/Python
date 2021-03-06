from django.contrib import admin

from mysite2.supperMarket.models import MainSort, SubSort, ImagePath, Item, Brand, Kind


class MainSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby', 'linkURL', 'onClick', 'devId', 'devClass')
        
class SubSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby', 'mainSort', 'linkURL', 'onClick', 'devId', 'devClass')

class ImagePathAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby', 'mainSort','image1','image2','image3','image4','image5','image6','image7','image8','image9','image10','image11','image12','image13','image14','image15','link1','link2','link3','link4','link5','link6','link7','link8','link9','link10','link11','link12','link13','link14','link15')


class BrandAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name','sort')

class KindAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name','sort')

class ItemAdmin(admin.ModelAdmin):
    """
    """
    # name = models.CharField(max_length = 100)
    # marketPrice = models.IntegerField()
    # shorPrice = models.IntegerField()
    # imagePath = models.CharField(max_length = 500)
    # number = models.CharField(max_length = 20)
    # stock = models.IntegerField()
    # description = models.CharField(max_length = 2000)
    # brand = models.ForeignKey(Brand)
    # kind = models.ForeignKey(Kind)
    list_display = ('name', 'marketPrice', 'shorPrice', 'imagePath', 'number', 'stock', 'description', 'brand', 'kind', 'sort')
        


admin.site.register(MainSort, MainSortAdmin)
admin.site.register(SubSort, SubSortAdmin)
admin.site.register(ImagePath, ImagePathAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Kind, KindAdmin)

# Register your models here.
