from django.urls import re_path
from django.urls import include
from django.urls import path
from . import views


urlpatterns = (
	path('', views.produkt, name = 'produkts'),
	path('index.html', views.produkt, name = 'produkts'),
	path('special_offer.html', views.special_offer, name = 'special_offer'),
	path('dostavka.html', views.dostavka, name = 'dostavka'),
	path('contact.html', views.contact, name = 'contact'),
	path('product_summary.html', views.product_summary, name = 'product_summary'),
	re_path(r'product_details.html/$', views.product_details, name = 'product_details'),
)