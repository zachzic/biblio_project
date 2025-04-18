from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListeLivre.as_view(), name='liste_livre'),
    path('emprunts/', views.liste_emprunts, name='liste-emprunts'),
    path('emprunts/<int:emprunt_id>/retourner/', views.retourner_livre, name='retourner-livre'),
    path('livres/<int:livre_id>/emprunter/', views.emprunter_livre, name='emprunter-livre'),
]
