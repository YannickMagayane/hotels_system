from django.db import models
from reservation.models import Reservation

# Create your models here.
class Paiement(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="paiements")
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    methode = models.CharField(max_length=50, default='cinetpay')
    statut = models.CharField(
        max_length=20,
        choices=[('en_attente', 'En attente'), ('payé', 'Payé'), ('échoué', 'Échoué')],
        default='en_attente'
    )
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    date_paiement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Paiement {self.transaction_id} - {self.statut}"