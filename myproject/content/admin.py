from django.contrib import admin

# Register your models here.
from content.models import Category, Content, Images


class ContentImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'get_image_tag']
    list_filter = ['status']
    readonly_fields = ('get_image_tag',)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'detail', 'get_image_tag', 'status']
    readonly_fields = ('get_image_tag',)
    list_filter = ['status', 'category']
    inlines = [ContentImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'get_image_tag']
    readonly_fields = ('get_image_tag',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Images, ImagesAdmin)
