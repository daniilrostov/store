from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from produkt.models import Produkt


# Create your views here.

	
def produkt(request):	
	latest_produkt = Produkt.objects.all()
	return render(request, "index.html", {'latest_produkt' : latest_produkt})

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
	return render(request, "product_details.html", {'photo' : photo, 'photo1' : photo1, 'photo2' : photo2, 'photo3' : photo3, 'prise' : prise, 'name' : name})