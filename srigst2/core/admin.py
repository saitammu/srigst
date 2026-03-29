from django.contrib import admin
from .models import Enquiry

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'created_at', 'is_read')
    list_filter = ('is_read', 'service')
    search_fields = ('name', 'phone')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)

admin.site.site_header = 'Sri GST Interiors Admin'
admin.site.site_title = 'Sri GST Admin'
admin.site.index_title = 'Manage Enquiries'
