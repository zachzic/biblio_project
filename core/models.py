from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Auteur(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    date_publication = models.DateField()
    copies_disponibles = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)

    @property
    def est_retourne(self):
        return self.date_retour is not None

    def save(self, *args, **kwargs):
        if not self.pk:  # nouveau emprunt
            if self.livre.copies_disponibles > 0:
                self.livre.copies_disponibles -= 1
                self.livre.save()
            else:
                raise ValueError("Aucune copie disponible pour ce livre.")
        elif self.est_retourne and not Emprunt.objects.filter(pk=self.pk, date_retour__isnull=True).exists():
            # Livre est retourné, on incrémente le nombre de copies disponibles
            self.livre.copies_disponibles += 1
            self.livre.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.utilisateur.username} a emprunté {self.livre.titre} le {self.date_emprunt}"

