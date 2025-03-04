import pytest
from paiement.models import Paiement
from reservation.models import Reservation, Chambre, Hotel
from user.models import User
from datetime import date

@pytest.mark.django_db
def test_create_paiement():
    user = User.objects.create(email="testuser@example.com", first_name="Alex", last_name="Smith")
    hotel = Hotel.objects.create(nom="Hôtel de Paris", adresse="12 Rue Paris", telephone="5555555")
    chambre = Chambre.objects.create(hotel=hotel, numero="103", type="suite", prix=150.00)
    reservation = Reservation.objects.create(user=user, chambre=chambre, date_debut=date.today(), date_fin=date.today())
    paiement = Paiement.objects.create(reservation=reservation, montant=150.00, statut="payé", transaction_id="TX12345")
    assert paiement.statut == "payé"
    assert paiement.transaction_id == "TX12345"
