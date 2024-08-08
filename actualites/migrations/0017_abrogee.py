# Generated by Django 4.2.7 on 2024-07-08 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0016_legislationne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abrogee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('decret', 'Décret'), ('arrete', 'Arrêté'), ('loi', 'Loi'), ('convention', 'Convention et autres'), ('protocole', 'Protocole')], max_length=20)),
                ('titre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_publication', models.DateField(default=django.utils.timezone.now)),
                ('fichier_pdf', models.FileField(blank=True, null=True, upload_to='legislations_pdf/')),
            ],
            options={
                'ordering': ['-date_publication'],
            },
        ),
    ]
