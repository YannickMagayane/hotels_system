from django.test import TestCase
from django.contrib.admin.sites import site
from paiement.models import Paiement
from paiement.admin import PaiementAdmin

class AdminPaiementTest(TestCase):
    def test_paiement_admin_registered(self):
        """ Vérifie que le modèle Paiement est bien enregistré dans l'admin """
        self.assertTrue(site.is_registered(Paiement))

    def test_paiement_admin_list_display(self):
        """ Vérifie que les bons champs sont affichés dans l'admin """
        paiement_admin = PaiementAdmin(Paiement, site)
        expected_fields = ('reservation', 'montant', 'methode', 'statut', 'transaction_id', 'date_paiement')
        self.assertEqual(paiement_admin.list_display, expected_fields)

    def test_paiement_admin_list_filter(self):
        """ Vérifie que les filtres sont bien définis """
        paiement_admin = PaiementAdmin(Paiement, site)
        expected_filters = ('statut', 'methode', 'date_paiement')
        self.assertEqual(paiement_admin.list_filter, expected_filters)

    def test_paiement_admin_search_fields(self):
        """ Vérifie que les champs de recherche sont bien définis """
        paiement_admin = PaiementAdmin(Paiement, site)
        expected_search_fields = ('transaction_id', 'reservation__id')
        self.assertEqual(paiement_admin.search_fields, expected_search_fields)
