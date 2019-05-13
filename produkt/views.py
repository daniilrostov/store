from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from produkt.models import Produkt


# Create your views here.

	
def produkt(request):	
	produkt = Produkt.objects.filter(status='recomend')
	latest_produkt = Produkt.objects.filter(status='lost')
	tea_produkt = Produkt.objects.filter(group='tea')
	electronic_produkt = Produkt.objects.filter(group='electronic')
	tea_produkt_count = tea_produkt.count()
	electronic_produkt_count = electronic_produkt.count()
	group = [['Электроника', tea_produkt_count, 'Роутеры'], ['Чай', tea_produkt_count, 'Зелёный']]
	return render(request, "index.html", {'latest_produkt' : latest_produkt, 'produkt' : produkt,
	'group' : group})

def special_offer(request):
	return render(request, "special_offer.html")
	
def normal(request):
	return render(request, "normal.html")
	
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
	return render(request, "product_details.html", {'photo' : photo, 'photo1' : photo1, 
	'photo2' : photo2, 'photo3' : photo3, 'prise' : prise, 'name' : name, 'text' : text})