from django.test import TestCase
from django.contrib.admin.sites import site
from user.models import User
from user.admin import UserAdmin

class AdminUserTest(TestCase):
    def test_user_admin_registered(self):
        """ Vérifie que le modèle User est bien enregistré dans l'admin """
        self.assertTrue(site.is_registered(User))

    def test_user_admin_list_display(self):
        """ Vérifie que les bons champs sont affichés dans l'admin """
        user_admin = UserAdmin(User, site)
        expected_fields = ('email', 'first_name', 'last_name', 'poste', 'is_active', 'is_staff')
        self.assertEqual(user_admin.list_display, expected_fields)

    def test_user_admin_search_fields(self):
        """ Vérifie que la recherche fonctionne sur email, first_name et last_name """
        user_admin = UserAdmin(User, site)
        expected_search_fields = ('email', 'first_name', 'last_name')
        self.assertEqual(user_admin.search_fields, expected_search_fields)
