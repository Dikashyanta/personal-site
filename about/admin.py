from django.contrib import admin

# Register your models here.
# about/admin.py
from django.contrib import admin
from .models import HeroSection, CollagePhoto, Interest, Memory, MemoryPhoto

class CollagePhotoInline(admin.TabularInline):
    model = HeroSection.photo_collage.through
    extra = 3

class MemoryPhotoInline(admin.TabularInline):
    model = MemoryPhoto
    extra = 3

@admin.register(HeroSection)
class HeroAdmin(admin.ModelAdmin):
    fields = ['headline', 'intro_text', 'bio_letter']
    inlines = [CollagePhotoInline]

@admin.register(CollagePhoto)
class CollagePhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'order']

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'updated_at']

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'date', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MemoryPhotoInline]