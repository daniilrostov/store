# Generated by Django 2.0.10 on 2019-05-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkt', '0009_auto_20190507_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('text', models.CharField(max_length=199)),
                ('photo', models.ImageField(upload_to='media/')),
                ('photo1', models.ImageField(upload_to='media/')),
                ('photo2', models.ImageField(upload_to='media/')),
            ],
            options={
                'db_table': 'Settings',
            },
        ),
    ]
