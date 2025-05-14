from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import (
    Logo,
    Banner,
    Category,
    AboutCategory,
    Product,
    StoreInfo,
    SocialMedia,
    Partners,
    FooterText,
)


class IndexView(TemplateView):
    template_name = 'index.html'  # Asosiy sahifa

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos'] = Logo.objects.order_by('-id')[:1]
        context['banners'] = Banner.objects.order_by('-id')[:4]
        context['categories'] = Category.objects.order_by('-id')[:4]
        context['about'] = AboutCategory.objects.order_by('-id')[:1]
        context['products'] = Product.objects.order_by('-id')[:4]
        context['info'] = StoreInfo.objects.order_by('-id')[:1]
        context['media'] = SocialMedia.objects.all()
        context['partners'] = Partners.objects.all()
        context['footer'] = FooterText.objects.order_by('-id')[:1]
        return context


# 3️⃣ Kategoriya ro‘yxati va tafsiloti
class CategoryView(TemplateView):
    template_name = 'furniture.html'  # Kategoriyalar sahifasi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos'] = Logo.objects.all()
        context['categories'] = Category.objects.all()
        context['info'] = StoreInfo.objects.all()
        context['media'] = SocialMedia.objects.all()
        context['footer'] = FooterText.objects.order_by('-id')[:1]
        return context


# 4️⃣ About bo‘limi
class AboutView(TemplateView):
    template_name = 'about.html'  # About sahifasi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos'] = Logo.objects.all()
        context['about'] = AboutCategory.objects.order_by('-id')
        context['info'] = StoreInfo.objects.all()
        context['media'] = SocialMedia.objects.all()
        context['footer'] = FooterText.objects.order_by('-id')[:1]
        return context


# 5️⃣ Mahsulotlar (Products)
class ProductListView(TemplateView):
    template_name = 'shop.html'  # Maxsulotlar sahifasi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos'] = Logo.objects.all()
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.order_by('-id')
        context['info'] = StoreInfo.objects.all()
        context['media'] = SocialMedia.objects.all()
        context['footer'] = FooterText.objects.order_by('-id')[:1]
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logos'] = Logo.objects.all()
        context['info'] = StoreInfo.objects.order_by('-id')
        context['media'] = SocialMedia.objects.all()
        context['footer'] = FooterText.objects.order_by('-id')[:1]
        return context



