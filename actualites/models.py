from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    
class Statistic(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}: {self.value}"
    
class Personnel(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='personnel_photos/')
    linkedin = models.URLField()
    category = models.CharField(max_length=50, choices=[
        ('directeur', 'Directeur'),
        ('equipes', 'Equipes'),
        ('chefs_de_region', 'Chefs de région'),
    ])


class DirectorMessage(models.Model):
    image = models.ImageField(upload_to='director_messages/')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']    



class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualites/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Accords(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='actualites/', null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.title

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=20)
    description = models.TextField(max_length=500, default='default_description')
    image = models.ImageField(upload_to='projets/', null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titre

class Programme(models.Model):
    nom = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=20)
    description = models.TextField(max_length=500, default='default_description')
    image = models.ImageField(upload_to='programmes/', null=True, blank=True)
    date_creation = models.DateField()

    def __str__(self):
        return self.nom

class Journal(models.Model):
    titre = models.CharField(max_length=200)
    video = models.FileField(upload_to='journal_videos/', null=True, blank=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Rapports(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rapports/', null=True, blank=True)
    description = models.TextField(max_length=500, default='default_description')
    date_publication = models.DateTimeField(auto_now_add=True)
    fichier_pdf = models.FileField(upload_to='rapports_pdf/', null=True, blank=True)

    def __str__(self):
        return self.titre

class Feature(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='features/')
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Commentaire(models.Model):
    actualite = models.ForeignKey('Actualite', on_delete=models.CASCADE, related_name='commentaires')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    likes = models.IntegerField(default=0)
    date_creation = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='reponses')

    def __str__(self):
        return f"Commentaire de {self.nom} sur {self.actualite.titre}"

    class Meta:
        ordering = ['-date_creation']

class GalleryCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title or f"Image {self.id}"

class ContactMessage(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.prenom} {self.nom} - {self.date_envoi}"

    class Meta:
        ordering = ['-date_envoi']        




class Legislationne(models.Model):
    TYPES = (
        ('decret', 'Décret'),
        ('arrete', 'Arrêté'),
        ('loi', 'Loi'),
        ('convention', 'Convention et autres'),
        ('protocole', 'Protocole'),
    )
    
    type = models.CharField(max_length=20, choices=TYPES)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_publication = models.DateField(default=timezone.now)
    fichier_pdf = models.FileField(upload_to='legislations_pdf/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.titre}"

    class Meta:
        ordering = ['-date_publication']        




class Abrogee(models.Model):
    TYPES = (
        ('decret', 'Décret'),
        ('arrete', 'Arrêté'),
        ('loi', 'Loi'),
        ('convention', 'Convention et autres'),
        ('protocole', 'Protocole'),
    )
    
    type = models.CharField(max_length=20, choices=TYPES)
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_publication = models.DateField(default=timezone.now)
    fichier_pdf = models.FileField(upload_to='legislations_pdf/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_type_display()} - {self.titre}"

    class Meta:
        ordering = ['-date_publication']          