from django.contrib import admin
from .models import Hostgroup,Host,Region,Search

# Register your models here.
class HostAdmin(admin.ModelAdmin):
	list_display = ('hostname','eth0','eth1','group')
	search_fields= ('hostname','eth0','eth1','group')
	list_field = ('group',)
#	filter_horizontal = ('Region',)

admin.site.register(Hostgroup)
#admin.site.register(Host)
admin.site.register(Host,HostAdmin)
admin.site.register(Region)
admin.site.register(Search)
