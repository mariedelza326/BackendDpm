from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from actualites.views import (
    ActualiteViewSet, AccordsViewSet, ProjetViewSet, ProgrammeViewSet,LegislationViewSet,AbrogeeViewSet,StatisticViewSet,
    JournalViewSet, RapportsViewSet, FeatureViewSet, LoginView, RegisterView,GalleryCategoryViewSet,PersonnelViewSet,DirectorMessageViewSet,
    commentaire_list, repondre_commentaire, like_commentaire, supprimer_commentaire,
    send_message
)
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'actualites', ActualiteViewSet)
router.register(r'accords', AccordsViewSet)
router.register(r'projets', ProjetViewSet)
router.register(r'programmes', ProgrammeViewSet)
router.register(r'journal', JournalViewSet)
router.register(r'rapports', RapportsViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'gallery', GalleryCategoryViewSet)
router.register(r'legislations', LegislationViewSet)
router.register(r'abrogees', AbrogeeViewSet)
router.register(r'personnel', PersonnelViewSet)
router.register(r'director-messages', DirectorMessageViewSet)
router.register(r'statistics', StatisticViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/commentaires/', commentaire_list, name='creer-commentaire'),
    path('api/commentaires/<int:pk>/repondre/', repondre_commentaire, name='repondre-commentaire'),
    path('api/commentaires/<int:pk>/like/', like_commentaire, name='like-commentaire'),
    path('api/commentaires/<int:pk>/', supprimer_commentaire, name='supprimer-commentaire'),
    path('api/message/', send_message, name='send_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)