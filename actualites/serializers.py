from rest_framework import serializers
from .models import Personnel, Actualite, Accords,Projet,Programme,Journal,Rapports,Feature,Commentaire,CustomUser,ContactMessage,GalleryCategory,GalleryImage,Legislationne,Abrogee,DirectorMessage,Statistic


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ['id', 'name', 'value', 'description']
        
class DirectorMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorMessage
        fields = ['id', 'image', 'title', 'content', 'order']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class AbrogeeSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Abrogee
        fields = ['id', 'type', 'type_display', 'titre', 'description', 'date_publication', 'fichier_pdf']

class LegislationSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Legislationne
        fields = ['id', 'type', 'type_display', 'titre', 'description', 'date_publication', 'fichier_pdf']
class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'title']

class GalleryCategorySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = GalleryCategory
        fields = ['id', 'title', 'images']        

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = CustomUser

        fields = ['id', 'username', 'email', 'phone_number', 'password']

        extra_kwargs = {'password': {'write_only': True}}
        
class ActualiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actualite
        fields = ['id', 'titre', 'contenu', 'image', 'date_publication']

class AccordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accords
        fields = ['id', 'title', 'image', 'date_debut', 'date_fin']

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = ['id', 'titre', 'subtitle','description', 'image', 'date_debut', 'date_fin']

class ProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ['id', 'nom', 'subtitle','description', 'image', 'date_creation']



class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'titre','date_publication','video']                 


class RapportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rapports
        fields = ['id', 'titre', 'image', 'description', 'date_publication', 'fichier_pdf']        


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'title', 'image', 'description', 'order']        



class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = ['id', 'actualite', 'nom', 'email', 'contenu', 'date_creation', 'parent']

class ActualiteSerializer(serializers.ModelSerializer):
    commentaires = CommentaireSerializer(many=True, read_only=True)

    class Meta:
        model = Actualite
        fields = ['id', 'titre', 'contenu', 'image', 'date_publication', 'commentaires']

class ActualiteDetailSerializer(serializers.ModelSerializer):
    commentaires = serializers.SerializerMethodField()

    class Meta:
        model = Actualite
        fields = ['id', 'titre', 'contenu', 'image', 'date_publication', 'commentaires']

    def get_commentaires(self, obj):
        commentaires_principaux = Commentaire.objects.filter(actualite=obj, parent=None)
        return CommentaireSerializer(commentaires_principaux, many=True).data        