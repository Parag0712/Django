from django.contrib import admin
from .models import ChaiVarity,Notes,Certificate,ChaiReviw,Store
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviw
    extra = 2

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varity',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')

class NotesAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    
admin.site.register(ChaiVarity,ChaiVarityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Notes,NotesAdmin)
admin.site.register(Certificate,ChaiCertificateAdmin)