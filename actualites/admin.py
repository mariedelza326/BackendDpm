from django.contrib import admin
from .models import Actualite
from .models import Accords
from .models import Projet
from.models import Programme
from.models import Journal
from.models import Rapports
from.models import Feature
from.models import Commentaire
from.models import CustomUser
from.models import ContactMessage
from .models import GalleryCategory
from.models import GalleryImage
from .models import Legislationne
from .models import Abrogee
from .models import Personnel
from .models import DirectorMessage
from.models import Statistic




# Register your models here.

admin.site.register(Actualite)
admin.site.register(Accords)
admin.site.register(Projet)
admin.site.register(Programme)
admin.site.register(Journal)
admin.site.register(Rapports)
admin.site.register(Feature)
admin.site.register(Commentaire)
admin.site.register(CustomUser)
admin.site.register(ContactMessage)
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(Legislationne)
admin.site.register(Abrogee)
admin.site.register(Personnel)
admin.site.register(DirectorMessage)
admin.site.register(Statistic)