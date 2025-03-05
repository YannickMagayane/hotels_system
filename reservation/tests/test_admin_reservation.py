from django.test import TestCase
from django.contrib.admin.sites import site
from reservation.models import Reservation
from reservation.admin import ReservationAdmin

class AdminReservationTest(TestCase):
    def test_reservation_admin_registered(self):
        """ Vérifie que le modèle Reservation est bien enregistré dans l'admin """
        self.assertTrue(site.is_registered(Reservation))

    def test_reservation_admin_list_display(self):
        """ Vérifie que les champs affichés sont corrects """
        reservation_admin = ReservationAdmin(Reservation, site)
        expected_fields = ('user', 'chambre', 'date_debut', 'date_fin', 'statut')
        self.assertEqual(reservation_admin.list_display, expected_fields)

    def test_reservation_admin_list_filter(self):
        """ Vérifie que les filtres sont bien définis """
        reservation_admin = ReservationAdmin(Reservation, site)
        expected_filters = ('statut', 'date_debut', 'date_fin')
        self.assertEqual(reservation_admin.list_filter, expected_filters)

    def test_reservation_admin_search_fields(self):
        """ Vérifie que la recherche fonctionne sur email user, hôtel et numéro chambre """
        reservation_admin = ReservationAdmin(Reservation, site)
        expected_search_fields = ('user__email', 'chambre__hotel__nom', 'chambre__numero')
        self.assertEqual(reservation_admin.search_fields, expected_search_fields)

    def test_reservation_admin_date_hierarchy(self):
        """ Vérifie que la hiérarchie de date est bien définie """
        reservation_admin = ReservationAdmin(Reservation, site)
        self.assertEqual(reservation_admin.date_hierarchy, 'date_debut')
