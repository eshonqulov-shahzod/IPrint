from django.db import models

# Create your models here.


class Logo(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/display/')

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=25)  # Banner sarlavhasi
    subtitle = models.CharField(max_length=255, blank=True, null=True)  # Kichik sarlavha (bo'sh bo'lishi mumkin)
    description = models.TextField()  # Banner tavsifi
    photo = models.ImageField(upload_to='images/display/')  # Rasm yuklash uchun maydon
    video_url = models.URLField(blank=True, null=True)  # Video havolasi (majburiy emas)

    def __str__(self):
        return self.title  # Admin panelda banner nomi sifatida chiqadi


# Umumiy kategoriya modeli

#class Category(models.Model):
#    name = models.CharField(max_length=100, unique=True)  # Kategoriya nomi
#    photo = models.ImageField(upload_to='images/display/')  # Kategoriya rasmi
#
#    def __str__(self):
#        return self.name
#

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return f"{self.category.name} image"

# About bo'limi uchun kategoriya


class AboutCategory(models.Model):
    title = models.CharField(max_length=255)  # "About Us" sarlavhasi
    description = models.TextField()  # Tavsif matni
    photo = models.ImageField(upload_to='images/display/')  # Rasm yuklash
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='about_categories',
        verbose_name="Kategoriya"
    )

    def __str__(self):
        return self.title


# Mahsulotlar bo'limi uchun kategoriya
class Product(models.Model):
    name = models.CharField(max_length=255)  # Mahsulot nomi (Chairs, Tables, etc.)
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Narx (masalan, $100.00)
    photo = models.ImageField(upload_to='images/display/')  # Mahsulot rasmi
    is_new = models.BooleanField(default=False)  # "New" yorlig‘ini qo‘yish uchun
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product_categories',
        verbose_name="Kategoriya"
    )

    def __str__(self):
        return self.name


# 1️⃣ Do‘kon haqida asosiy ma'lumotlar

class StoreInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name="Manzil")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    google_map_url = models.TextField(verbose_name="Google Map Manzili")  # URLField emas!
    telegram_url = models.URLField(verbose_name="Telegram manzil", blank=True, null=True)

    def __str__(self):
        return self.address


# 2️⃣ Ijtimoiy tarmoqlar uchun model

class SocialMedia(models.Model):
    PLATFORM_CHOICES = [
        ('telegram', 'Telegram'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('olx', 'OLX'),
    ]
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, verbose_name="Platforma")
    url = models.URLField(verbose_name="Havola")

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"


class Partners(models.Model):
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/display/')


class FooterText(models.Model):
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)


