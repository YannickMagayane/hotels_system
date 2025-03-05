from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'montant', 'methode', 'statut', 'transaction_id', 'date_paiement')
    list_filter = ('statut', 'methode', 'date_paiement')
    search_fields = ('transaction_id', 'reservation__id')
    date_hierarchy = 'date_paiement'
