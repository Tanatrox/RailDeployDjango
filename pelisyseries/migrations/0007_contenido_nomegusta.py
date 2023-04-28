# Generated by Django 4.1 on 2022-11-05 06:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pelisyseries', '0006_contenido_megusta'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido',
            name='noMeGusta',
            field=models.ManyToManyField(related_name='No_Me_Gusta', to=settings.AUTH_USER_MODEL),
        ),
    ]