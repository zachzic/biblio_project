from django.views.generic import ListView
from .models import Livre, Emprunt
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from .models import Emprunt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib import messages

#Par défaut, ListView effectue une requête SELECT * FROM Livre
class ListeLivre(ListView):
    model = Livre
    template_name = "core/liste_livre.html"
    context_object_name = "livres"


@require_POST
@login_required
def retourner_livre(request, emprunt_id):
    """Gérer le retour d'un livre (POST uniquement)."""
    emprunt = get_object_or_404(Emprunt, pk=emprunt_id, utilisateur=request.user)

    if not emprunt.est_retourne:
        emprunt.date_retour = timezone.now()
        emprunt.livre.copies_disponibles += 1  #Incrémenter ici
        emprunt.livre.save()
        emprunt.save()
        messages.success(request, f"📕 Livre « {emprunt.livre.titre} » retourné avec succès.")
    else:
        messages.warning(request, "⛔ Ce livre a déjà été retourné.")
        
    return redirect('liste-emprunts')

#@require_POST
@login_required
def liste_emprunts(request):
    emprunts = Emprunt.objects.filter(utilisateur=request.user)

    return render(request, 'core/liste_emprunts.html', {'emprunts': emprunts})

@require_POST
@login_required
def emprunter_livre(request, livre_id):
    livre = get_object_or_404(Livre, id=livre_id)

    # Vérification du nombre d'emprunts en cours
    emprunts_en_cours = Emprunt.objects.filter(utilisateur=request.user, date_retour__isnull=True).count()
    if emprunts_en_cours >= 3:
        messages.warning(request, "🚫 Vous avez déjà 3 emprunts en cours. Veuillez en retourner un avant d'emprunter un nouveau livre.")
        return redirect('liste_livre')

    # Vérifie qu'il reste des copies
    if livre.copies_disponibles <= 0:
        messages.error(request, "😕 Aucune copie disponible pour ce livre.")
        return redirect('liste_livre')

    # Création de l'emprunt
    Emprunt.objects.create(utilisateur=request.user, livre=livre)
    messages.success(request, f"✅ Livre « {livre.titre} » emprunté avec succès !")
    return redirect('liste-emprunts')