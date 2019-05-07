from django.db import models

# Create your models here.
GROUP = (
    ('electronic','Электроника'),
    ('tea', 'Чай'),
)
STATUS = (
    ('lost','Новое'),
    ('recomend', 'Рекомендуемое'),
)
class Produkt(models.Model):
	name = models.CharField(max_length = 40)
	group = models.CharField(max_length = 40, choices=GROUP, default='electronics')
	status = models.CharField(max_length = 40, choices=STATUS, default='Новое')
	text = models.CharField(max_length = 199)
	prise = models.IntegerField(default=1)
	photo = models.ImageField(upload_to='media/', null=False) 
	photo1 = models.ImageField(upload_to='media/', null=True)
	photo2 = models.ImageField(upload_to='media/', null=True)
	photo3 = models.ImageField(upload_to='media/', null=True)



	def __str__(self):
		return self.name
	
	class Meta:
		db_table = "Produkt"