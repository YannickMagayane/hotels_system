from django.urls import path
from . import views

urlpatterns = [
    # Hôtel
    path('', views.hotel_list, name='hotel_list'),
    path('hotel/create/', views.hotel_create, name='hotel_create'),
    path('hotel/<int:pk>/edit/', views.hotel_update, name='hotel_update'),
    path('hotel/<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),
    path('hotel/<int:pk>/', views.hotel_detail, name='hotel_detail'),

    # Chambre
    path('chambres/', views.chambre_list, name='chambre_list'),
    path('chambre/create/', views.chambre_create, name='chambre_create'),
    path('chambre/<int:pk>/edit/', views.chambre_update, name='chambre_update'),
    path('chambre/<int:pk>/delete/', views.chambre_delete, name='chambre_delete'),
    path('chambre/<int:pk>/', views.chambre_detail, name='chambre_detail'),

    # Photo Chambre
    path('chambre/<int:chambre_pk>/photo/create/', views.photo_chambre_create, name='photo_chambre_create'),
    path('photo/<int:pk>/delete/', views.photo_chambre_delete, name='photo_chambre_delete'),

    # Réservation
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservation/create/', views.reservation_create, name='reservation_create'),
    path('reservation/<int:pk>/edit/', views.reservation_update, name='reservation_update'),
    path('reservation/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),
    path('reservation/<int:pk>/', views.reservation_detail, name='reservation_detail'),
]
