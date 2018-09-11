from django.db import models

# Create your models here.

class Produkt(models.Model):
	name = models.CharField(max_length = 40)
	text = models.CharField(max_length = 199)
	prise = models.IntegerField(default=1)
	photo = models.ImageField(upload_to='media/', null=False) 
	photo1 = models.ImageField(upload_to='media/', null=True)
	photo2 = models.ImageField(upload_to='media/', null=True)
	photo3 = models.ImageField(upload_to='media/', null=True)
#	photo4 = models.ImageField(upload_to='media/', null=False)
#	photo5 = models.ImageField(upload_to='media/', null=False)
#	photo6 = models.ImageField(upload_to='media/', null=False)
#	photo7 = models.ImageField(upload_to='media/', null=False)

	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "Produkt"