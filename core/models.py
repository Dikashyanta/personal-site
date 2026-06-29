from django.db import models


class SiteSettings(models.Model):
    """
    Singleton model — only one row should ever exist.
    Admins control the hero section content, logo, and profile photo here.
    """

    # --- Logo ---
    logo_text = models.CharField(
        max_length=20,
        default="D.",
        help_text="Short text shown as the navbar logo (e.g. 'D.').",
    )
    logo_image = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True,
        help_text="Optional logo image. If set, it replaces the logo text in the navbar.",
    )

    # --- Hero highlight colour ---
    hero_highlight_color = models.CharField(
        max_length=20,
        default="#b8d4f0",
        help_text="CSS colour value for the blue highlight behind the hero name/bio (e.g. #b8d4f0).",
    )

    # --- Hero text ---
    hero_eyebrow = models.CharField(
        max_length=100,
        default="est. 2003 · kathmandu",
        help_text="Small text above the hero name.",
    )
    hero_name = models.CharField(
        max_length=100,
        default="Handsome Dikshyant.",
        help_text="Main hero heading (your name).",
    )
    hero_bio = models.TextField(
        default="Builder of things. Collector of moments.\nThis isn't a portfolio — it's my life, written down.",
        help_text="Short bio shown below the name. Use a newline for a line break.",
    )
    hero_handle = models.CharField(
        max_length=60,
        default="@dikashyanta",
        help_text="Social handle shown below the bio.",
    )

    # --- Hero photo ---
    hero_photo = models.ImageField(
        upload_to="site/",
        blank=True,
        null=True,
        help_text="Profile photo shown on the right side of the hero section.",
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        # Enforce singleton — always reuse the same row (pk=1)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        """Return the single SiteSettings instance, creating defaults if needed."""
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
