from django.contrib import admin

from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'category', 'date_display', 'created_at')
    search_fields = ('title', 'issuer', 'category')
    list_filter = ('category',)
