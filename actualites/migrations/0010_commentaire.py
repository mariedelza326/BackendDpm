# Generated by Django 4.2.7 on 2024-06-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0009_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contenu', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('actualite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='actualites.actualite')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reponses', to='actualites.commentaire')),
            ],
            options={
                'ordering': ['-date_creation'],
            },
        ),
    ]
