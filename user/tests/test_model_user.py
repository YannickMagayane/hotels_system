from django.test import TestCase
from django.core.exceptions import ValidationError
from user.models import User

class UserModelTest(TestCase):

    def setUp(self):
        """Nettoyage de la base de données avant chaque test"""
        User.objects.all().delete()

    def test_invalid_email(self):
        """Vérifie que l'email doit être unique"""
        # Création d'un utilisateur avec un email valide
        User.objects.create_user(
            email="user1@example.com", first_name="Valid", last_name="Email", poste="client", password="password"
        )

        # Test pour vérifier l'unicité de l'email
        with self.assertRaises(ValidationError):
            User.objects.create_user(
                email="user1@example.com", first_name="Invalid", last_name="Email", poste="client", password="password"
            )
