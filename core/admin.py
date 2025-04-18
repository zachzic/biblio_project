from django.contrib import admin
from .models import Auteur, Categorie, Livre, Emprunt


@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'categorie', 'date_publication', 'copies_disponibles')
    search_fields = ('titre',)

@admin.register(Auteur)
class AuteurAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)


#admin.site.register(Auteur)
admin.site.register(Categorie)
#admin.site.register(Livre)
#admin.site.register(Emprunt)


#algo passme
