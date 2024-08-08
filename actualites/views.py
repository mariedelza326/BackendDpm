from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Actualite, Accords, Projet, Programme, Journal, Rapports, Feature, Commentaire,CustomUser,ContactMessage,GalleryCategory,Legislationne,Abrogee,Personnel,DirectorMessage,Statistic
from .serializers import (
    ActualiteSerializer, AccordsSerializer, ProjetSerializer, ProgrammeSerializer,PersonnelSerializer,
    JournalSerializer, RapportsSerializer, FeatureSerializer, CommentaireSerializer, ActualiteDetailSerializer,CustomUserSerializer,ContactMessageSerializer,GalleryCategorySerializer,LegislationSerializer,AbrogeeSerializer,DirectorMessageSerializer,StatisticSerializer,
)



@api_view(['GET', 'POST'])
def send_message(request):
    if request.method == 'GET':
        messages = ContactMessage.objects.all()
        serializer = ContactMessageSerializer(messages, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class RegisterView(APIView):

    def post(self, request):

        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GalleryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryCategory.objects.all()
    serializer_class = GalleryCategorySerializer

class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer
    
class PersonnelViewSet(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class DirectorMessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DirectorMessage.objects.all()
    serializer_class = DirectorMessageSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            # Ici, vous pouvez ajouter la logique pour créer un token si nécessaire
            return Response({'message': 'Logged in successfully', 'username': username}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class ActualiteViewSet(viewsets.ModelViewSet):
    queryset = Actualite.objects.all()
    serializer_class = ActualiteSerializer

class AccordsViewSet(viewsets.ModelViewSet):
    queryset = Accords.objects.all()
    serializer_class = AccordsSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class ProgrammeViewSet(viewsets.ModelViewSet):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer

class LegislationViewSet(viewsets.ModelViewSet):
    queryset = Legislationne.objects.all()
    serializer_class = LegislationSerializer

class AbrogeeViewSet(viewsets.ModelViewSet):
    queryset = Abrogee.objects.all()
    serializer_class = AbrogeeSerializer
class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class RapportsViewSet(viewsets.ModelViewSet):
    queryset = Rapports.objects.all()
    serializer_class = RapportsSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class ActualiteDetailView(generics.RetrieveAPIView):
    queryset = Actualite.objects.all()
    serializer_class = ActualiteDetailSerializer

@api_view(['GET', 'POST'])
def commentaire_list(request):
    if request.method == 'GET':
        commentaires = Commentaire.objects.all()
        serializer = CommentaireSerializer(commentaires, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def repondre_commentaire(request, pk):
    try:
        parent_comment = Commentaire.objects.get(pk=pk)
    except Commentaire.DoesNotExist:
        return Response(status=404)

    serializer = CommentaireSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(parent=parent_comment, actualite=parent_comment.actualite)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def like_commentaire(request, pk):
    try:
        commentaire = Commentaire.objects.get(pk=pk)
        commentaire.likes += 1
        commentaire.save()
        return Response({'likes': commentaire.likes}, status=status.HTTP_200_OK)
    except Commentaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def supprimer_commentaire(request, pk):
    try:
        commentaire = Commentaire.objects.get(pk=pk)
        commentaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Commentaire.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    