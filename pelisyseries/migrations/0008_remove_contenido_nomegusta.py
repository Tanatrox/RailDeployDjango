# Generated by Django 4.1 on 2022-11-05 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelisyseries', '0007_contenido_nomegusta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenido',
            name='noMeGusta',
        ),
    ]
