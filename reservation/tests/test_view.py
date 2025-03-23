import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from reservation.models import Hotel, Chambre, Reservation

@pytest.mark.django_db
def test_hotel_list_view(client):
    Hotel.objects.create(nom="Hotel Test", adresse="123 Rue Exemple", telephone="0123456789")
    response = client.get(reverse('hotel_list'))
    assert response.status_code == 200
    assert b'Hotel Test' in response.content

@pytest.mark.django_db
def test_hotel_create_view(client):
    response = client.post(reverse('hotel_create'), {
        'nom': 'Hotel Nouveau',
        'adresse': '456 Rue Test',
        'telephone': '9876543210'
    })
    assert response.status_code == 302
    assert Hotel.objects.filter(nom='Hotel Nouveau').exists()

@pytest.mark.django_db
def test_hotel_update_view(client):
    hotel = Hotel.objects.create(nom="Hotel Update", adresse="Update Adresse", telephone="0101010101")
    response = client.post(reverse('hotel_update', args=[hotel.id]), {
        'nom': 'Hotel Modifié',
        'adresse': 'Nouvelle Adresse',
        'telephone': '0202020202'
    })
    hotel.refresh_from_db()
    assert response.status_code == 302
    assert hotel.nom == 'Hotel Modifié'

@pytest.mark.django_db
def test_hotel_delete_view(client):
    hotel = Hotel.objects.create(nom="Hotel Supprimé", adresse="Adresse Supp", telephone="0303030303")
    response = client.post(reverse('hotel_delete', args=[hotel.id]))
    assert response.status_code == 302
    assert not Hotel.objects.filter(id=hotel.id).exists()

@pytest.mark.django_db
def test_chambre_list_view(client):
    hotel = Hotel.objects.create(nom="Hotel Test", adresse="123 Rue Exemple", telephone="0123456789")
    Chambre.objects.create(hotel=hotel, numero="101", type="simple", prix=100.0, disponible=True)
    response = client.get(reverse('chambre_list'))
    assert response.status_code == 200
    assert b'101' in response.content

@pytest.mark.django_db
def test_reservation_create_view(client, django_user_model):
    user = django_user_model.objects.create_user(
        email="testuser@example.com",
        password="password123"
    )

    client.force_login(user)  # Utiliser force_login pour s'assurer que l'utilisateur est connecté
    assert '_auth_user_id' in client.session  # Vérifie la connexion

    hotel = Hotel.objects.create(nom="Hotel Test", adresse="123 Rue Exemple", telephone="0123456789")
    chambre = Chambre.objects.create(hotel=hotel, numero="102", type="double", prix=120.0, disponible=True)

    response = client.post(reverse('reservation_create'), {
        'user': user.id,
        'chambre': chambre.id,  # Assurez-vous que la chambre existe
        'date_debut': '2025-01-01',
        'date_fin': '2025-01-05',
        'statut': 'en_attente'
    })

    if response.status_code == 200:  # Vérifie s'il y a des erreurs de formulaire
        print(response.context['form'].errors)

    assert response.status_code == 302  # Vérifie la redirection après création
