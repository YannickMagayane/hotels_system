import pytest
from reservation.models import Hotel, Chambre, Reservation, PhotoChambre
from user.models import User
from datetime import date

@pytest.mark.django_db
def test_create_hotel():
    hotel = Hotel.objects.create(nom="Grand Hôtel", adresse="123 Avenue", telephone="123456789")
    assert hotel.nom == "Grand Hôtel"

@pytest.mark.django_db
def test_create_chambre():
    hotel = Hotel.objects.create(nom="Hôtel Test", adresse="456 Rue", telephone="987654321")
    chambre = Chambre.objects.create(hotel=hotel, numero="101", type="double", prix=100.50)
    assert chambre.numero == "101"

@pytest.mark.django_db
def test_create_reservation():
    user = User.objects.create(email="client@example.com", first_name="Jean", last_name="Dupont")
    hotel = Hotel.objects.create(nom="Hôtel Royal", adresse="789 Boulevard", telephone="123123123")
    chambre = Chambre.objects.create(hotel=hotel, numero="102", type="suite", prix=200.00)
    reservation = Reservation.objects.create(user=user, chambre=chambre, date_debut=date.today(), date_fin=date.today())
    assert reservation.chambre == chambre
    assert reservation.user == user
