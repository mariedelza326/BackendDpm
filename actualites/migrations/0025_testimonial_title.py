# Generated by Django 3.2 on 2024-07-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0024_testimonial_cible'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]