from django.db import models

# Create your models here.

# about/models.py

class HeroSection(models.Model):
    headline       = models.CharField(max_length=200)
    bio_letter     = models.TextField()
    photo_collage  = models.ManyToManyField('CollagePhoto')

class CollagePhoto(models.Model):
    image     = models.ImageField(upload_to='collage/')
    order     = models.PositiveIntegerField(default=0)

class Interest(models.Model):
    CATEGORY_CHOICES = [
        ('reading',   'Reading'),
        ('building',  'Building'),
        ('listening', 'Listening'),
        ('where',     'Where'),
    ]
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    icon        = models.CharField(max_length=50, blank=True)
    updated_at  = models.DateTimeField(auto_now=True)

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
