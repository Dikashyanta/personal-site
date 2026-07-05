from django.db import models

# Create your models here.

# about/models.py

class HeroSection(models.Model):
    headline       = models.CharField(max_length=200)
    intro_text     = models.TextField(default='Not a resume. Not a portfolio.\nJust a person trying to build things,\nsee places, and remember it all.')
    bio_letter     = models.TextField()
    photo_collage  = models.ManyToManyField('CollagePhoto')

class CollagePhoto(models.Model):
    image     = models.ImageField(upload_to='collage/')
    order     = models.PositiveIntegerField(default=0)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Interest(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='interests',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='interests/covers/')
    updated_at = models.DateTimeField(auto_now=True)

class Memory(models.Model):
    title        = models.CharField(max_length=200)
    caption      = models.CharField(max_length=300)
    cover_image  = models.ImageField(upload_to='memories/covers/')
    story        = models.TextField()
    date         = models.DateField()
    slug         = models.SlugField(unique=True)
    created_at   = models.DateTimeField(auto_now_add=True)

class MemoryPhoto(models.Model):
    memory  = models.ForeignKey(Memory, on_delete=models.CASCADE, related_name='photos')
    image   = models.ImageField(upload_to='memories/photos/')
    caption = models.CharField(max_length=200, blank=True)
    order   = models.PositiveIntegerField(default=0)
