from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
    Logo,
    Banner,
    Category,
    AboutCategory,
    Product,
    SocialMedia,
    StoreInfo,
    Partners,
    CategoryImage,
    FooterText,

)

# Register your models here.


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage
    extra = 4
    max_num = 4


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryImageInline]


admin.site.register(Category, CategoryAdmin)

admin.site.register(Logo)
admin.site.register(Banner)
admin.site.register(AboutCategory)
admin.site.register(Product)
admin.site.register(SocialMedia)
admin.site.register(StoreInfo)
admin.site.register(Partners)
admin.site.register(FooterText)
