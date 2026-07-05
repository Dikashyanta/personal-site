from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Category, HeroSection, CollagePhoto, Interest, Memory, MemoryPhoto

class CollagePhotoInline(admin.TabularInline):
    model = HeroSection.photo_collage.through
    extra = 0
    
    def get_queryset(self, request):
        # Remove any potential duplicates
        qs = super().get_queryset(request)
        return qs.distinct()

class MemoryPhotoInline(admin.TabularInline):
    model = MemoryPhoto
    extra = 3

@admin.register(HeroSection)
class HeroAdmin(admin.ModelAdmin):
    fields = ['headline', 'intro_text', 'bio_letter']
    inlines = [CollagePhotoInline]
    
    def get_inline_instances(self, request, obj=None):
        # Only show inlines when editing existing HeroSection
        if obj is None:
            return []
        return super().get_inline_instances(request, obj)

@admin.register(CollagePhoto)
class CollagePhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'order']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'updated_at']
    list_filter = ['category']

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display  = ['title', 'date', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [MemoryPhotoInline]