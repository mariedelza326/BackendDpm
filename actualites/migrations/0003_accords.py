# Generated by Django 4.2.7 on 2024-06-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0002_alter_actualite_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='actualites/')),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
            ],
        ),
    ]
