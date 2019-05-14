from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from produkt.models import Produkt, Settings


# Create your views here.

	
def produkt(request):	
	produkt = Produkt.objects.filter(status='recomend')
	latest_produkt = Produkt.objects.filter(status='lost')
	tea_produkt = Produkt.objects.filter(group='tea')
	electronic_produkt = Produkt.objects.filter(group='electronic')
	tea_produkt_count = tea_produkt.count()
	electronic_produkt_count = electronic_produkt.count()
	carusel = Settings.objects.get(name='carusel')
	return render(request, "index.html", {'carusel' : carusel, 'latest_produkt' : latest_produkt, 'produkt' : produkt, 'tea_produkt' : tea_produkt, 'tea_produkt_count' : tea_produkt_count, 'electronic_produkt' : electronic_produkt, 'electronic_produkt_count': electronic_produkt_count})

def special_offer(request):
	return render(request, "special_offer.html")
	
def dostavka(request):
	produkt = Produkt.objects.filter(status='recomend')
	latest_produkt = Produkt.objects.filter(status='lost')
	tea_produkt = Produkt.objects.filter(group='tea')
	electronic_produkt = Produkt.objects.filter(group='electronic')
	tea_produkt_count = tea_produkt.count()
	electronic_produkt_count = electronic_produkt.count()
	dostavka = Settings.objects.get(name='dostavka')
	return render(request, "dostavka.html", {'dostavka' : dostavka, 'latest_produkt' : latest_produkt, 'produkt' : produkt, 'tea_produkt' : tea_produkt, 'tea_produkt_count' : tea_produkt_count, 'electronic_produkt' : electronic_produkt, 'electronic_produkt_count': electronic_produkt_count})
	
def contact(request):
	produkt = Produkt.objects.filter(status='recomend')
	latest_produkt = Produkt.objects.filter(status='lost')
	tea_produkt = Produkt.objects.filter(group='tea')
	electronic_produkt = Produkt.objects.filter(group='electronic')
	tea_produkt_count = tea_produkt.count()
	electronic_produkt_count = electronic_produkt.count()
	contact = Settings.objects.get(name='contact')
	return render(request, "contact.html", {'contact' : contact, 'latest_produkt' : latest_produkt, 'produkt' : produkt, 'tea_produkt' : tea_produkt, 'tea_produkt_count' : tea_produkt_count, 'electronic_produkt' : electronic_produkt, 'electronic_produkt_count': electronic_produkt_count})	
	
def product_details(request):
	id = request.GET.get('id')
	detail_produkt = Produkt.objects.get( name=id )
	photo = detail_produkt.photo
	photo1 = detail_produkt.photo1
	photo2 = detail_produkt.photo2
	photo3 = detail_produkt.photo3
	prise = detail_produkt.prise
	name = detail_produkt.name
	text = detail_produkt.text
	tea_produkt = Produkt.objects.filter(group='tea')
	electronic_produkt = Produkt.objects.filter(group='electronic')
	tea_produkt_count = tea_produkt.count()
	electronic_produkt_count = electronic_produkt.count()
	return render(request, "product_details.html", {'photo' : photo, 'photo1' : photo1, 'photo2' : photo2, 'photo3' : photo3, 'prise' : prise, 'name' : name, 'text' : text, 'tea_produkt' : tea_produkt, 'tea_produkt_count' : tea_produkt_count, 'electronic_produkt' : electronic_produkt, 'electronic_produkt_count': electronic_produkt_count})