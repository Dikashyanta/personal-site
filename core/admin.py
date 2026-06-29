from django.contrib import admin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Logo",
            {
                "fields": ["logo_text", "logo_image"],
                "description": "Controls the logo shown in the navbar. Upload an image to replace the text logo.",
            },
        ),
        (
            "Hero Section — Highlight",
            {
                "fields": ["hero_highlight_color"],
                "description": "CSS colour for the blue-ish highlight box behind the hero name and bio.",
            },
        ),
        (
            "Hero Section — Text",
            {
                "fields": [
                    "hero_eyebrow",
                    "hero_name",
                    "hero_bio",
                    "hero_handle",
                ],
            },
        ),
        (
            "Hero Section — Photo",
            {
                "fields": ["hero_photo"],
                "description": "Profile photo shown on the right side of the hero section.",
            },
        ),
    ]

    def has_add_permission(self, request):
        # Only allow one instance — hide the 'Add' button if one already exists
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the singleton row
        return False
