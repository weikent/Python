from django.contrib import admin

from mysite2.supperMarket.models import MainSort, SubSort, ImagePath


class MainSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby')
        
class SubSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby', 'mainSort')

class ImagePathAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'image1','image2','image3','image4','image5','image6','image7','image8','image9','image10','image11','image12','image13','image14','image15')

admin.site.register(MainSort, MainSortAdmin)
admin.site.register(SubSort, SubSortAdmin)
admin.site.register(ImagePath, ImagePathAdmin)

# Register your models here.
