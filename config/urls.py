from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('aegiscontrol/', admin.site.urls),
    path('', include('home.urls')),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('home.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
