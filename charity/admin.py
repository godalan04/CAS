from django.contrib import admin
from charity.models import Charity
# Register your models here.
@admin.register(Charity)
class CharityAdmin(admin.ModelAdmin):
    list_display = ['name','description','url','get_tags']

    def get_tags(self,obj):
        return ", ".join( o for o in obj.tags.names())