from modeltranslation.translator import register, TranslationOptions, translator
from .models import Logo, Banner, Category, AboutCategory, Product, StoreInfo, Partners, FooterText


@register(Logo)
class LogoTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(AboutCategory)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'is_new')


@register(StoreInfo)
class StoreInfoTranslationOptions(TranslationOptions):
    fields = ('address', )


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(FooterText)
class FooterTextTranslationOptions(TranslationOptions):
    fields = ('name', 'description')