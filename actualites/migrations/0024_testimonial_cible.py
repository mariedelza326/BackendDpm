# Generated by Django 3.2 on 2024-07-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0023_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='cible',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
