from django.db import models
from user.model import User


class Hotel(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom


class Chambre(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="chambres")
    numero = models.CharField(max_length=10, unique=True)
    type = models.CharField(
        max_length=50,
        choices=[('simple', 'Simple'), ('double', 'Double'), ('suite', 'Suite')]
    )
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hotel.nom} - Chambre {self.numero}"


class PhotoChambre(models.Model):
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="chambres_photos/")

    def __str__(self):
        return f"Photo {self.id} - {self.chambre}"



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chambre = models.ForeignKey(Chambre, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    statut = models.CharField(
        max_length=20,
        choices=[('en_attente', 'En attente'), ('confirmée', 'Confirmée'), ('annulée', 'Annulée')],
        default='en_attente'
    )

    def __str__(self):
        return f"Réservation {self.id} - {self.user.first_name}"



