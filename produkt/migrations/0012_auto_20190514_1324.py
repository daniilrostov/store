# Generated by Django 2.0.10 on 2019-05-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0011_auto_20190514_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='status',
            field=models.CharField(choices=[('lost', 'Новое'), ('recomend', 'Рекомендуемое'), ('standart', 'Стандарт')], default='Новое', max_length=40),
        ),
    ]
