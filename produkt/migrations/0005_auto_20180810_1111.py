# Generated by Django 2.2 on 2018-08-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0004_produkt_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]