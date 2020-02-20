from django.contrib import admin
# Register your models here.
from .models import Listing


# this class shows what is to be displayed in the admin area

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')  # activating the links
    list_filter = ('realtor',)  # filter by name
    list_editable = ('is_published',)  # to publish or unpublish
    search_fields = ('title', 'description', 'address', 'city',
                     'state', 'zipcode', 'price')  # creates a searchbox
    list_per_page= 25


admin.site.register(Listing, ListingAdmin)
