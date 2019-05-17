from django.db import models
from setuptools._vendor.six import _meth_self
#from django import forms

# Create your models here.
GROUP = (
    ('electronic','Электроника'),
    ('tea', 'Чай'),
)
STATUS = (
    ('lost','Новое'),
    ('recomend', 'Рекомендуемое'),
    ('standart', 'Стандарт'),
)
class Produkt(models.Model):
	name = models.CharField(max_length = 40)
	group = models.CharField(max_length = 40, choices=GROUP, default='electronics')
	status = models.CharField(max_length = 40, choices=STATUS, default='Новое')
	text = models.CharField(max_length = 199)
	prise = models.IntegerField(default=1)
	photo = models.ImageField(upload_to='media/', null=False) 
	photo1 = models.ImageField(upload_to='media/', null=True, blank=True)
	photo2 = models.ImageField(upload_to='media/', null=True, blank=True)
	photo3 = models.ImageField(upload_to='media/', null=True, blank=True)
 
	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "Produkt"

class Settings(models.Model):
	name = models.CharField(max_length = 40)
	text = models.CharField(max_length = 199, blank=True)
	photo = models.ImageField(upload_to='media/', blank=True) 
	photo1 = models.ImageField(upload_to='media/', blank=True)
	photo2 = models.ImageField(upload_to='media/', blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "Settings"
		

class Subscribers(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=128)
	
	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "Subscribers"














