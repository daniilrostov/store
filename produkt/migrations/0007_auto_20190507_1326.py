# Generated by Django 2.0.10 on 2019-05-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0006_auto_20180810_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkt',
            name='group',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produkt',
            name='status',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
