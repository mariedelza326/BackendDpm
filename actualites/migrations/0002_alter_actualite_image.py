# Generated by Django 4.2.7 on 2024-06-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualite',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='actualites/'),
        ),
    ]
