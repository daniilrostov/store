# Generated by Django 2.0.10 on 2019-05-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0008_auto_20190507_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='group',
            field=models.CharField(choices=[('electronic', 'Электроника'), ('tea', 'Чай')], default='electronics', max_length=40),
        ),
        migrations.AlterField(
            model_name='produkt',
            name='status',
            field=models.CharField(choices=[('lost', 'Новое'), ('recomend', 'Рекомендуемое')], default='Новое', max_length=40),
        ),
    ]
