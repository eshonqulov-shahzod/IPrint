from django.urls import path
from .views import (
    IndexView,
    CategoryView,
    AboutView,
    ProductListView,
    ContactView)


urlpatterns = [
    path('', IndexView.as_view(),  name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('furniture/', CategoryView.as_view(), name='furniture'),
    path('shop/', ProductListView.as_view(), name='shop'),
    ]




