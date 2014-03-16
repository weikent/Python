from django.contrib import admin

from mysite2.supperMarket.models import MainSort, SubSort


class MainSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby')
        
class SubSortAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('name', 'sortby', 'mainSort')


admin.site.register(MainSort, MainSortAdmin)
admin.site.register(SubSort, SubSortAdmin)


# Register your models here.
