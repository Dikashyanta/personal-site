from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date_display = models.CharField(max_length=50)
    takeaway = models.TextField()
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} ({self.issuer})'
