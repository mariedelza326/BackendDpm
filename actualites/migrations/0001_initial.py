# Generated by Django 4.2.7 on 2024-06-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]