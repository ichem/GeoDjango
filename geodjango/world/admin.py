from django.contrib.gis import admin
from .models import WorldBorder

class WorldBorderAdmin(admin.GeoModelAdmin):
  search_fields = ['name']
  list_filter = ['region', 'subregion']
  list_display = ('name', 'area', 'pop2005')


admin.site.register(WorldBorder, WorldBorderAdmin)