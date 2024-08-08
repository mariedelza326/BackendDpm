# Generated by Django 4.2.7 on 2024-06-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0013_remove_customuser_nom_remove_customuser_prenom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_envoi'],
            },
        ),
    ]
