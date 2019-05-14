# Generated by Django 2.0.10 on 2019-05-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0010_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='text',
            field=models.CharField(blank=True, max_length=199),
        ),
    ]
