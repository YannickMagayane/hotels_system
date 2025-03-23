from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from .forms import HotelForm, ChambreForm, PhotoChambreForm, ReservationForm
from .models import Hotel, Chambre, PhotoChambre, Reservation

# Vues pour gérer l'Hotel

def hotel_list(request):
    hotels = Hotel.objects.all()
    chambres = Chambre.objects.select_related('hotel').prefetch_related('photos').all()
    return render(request, 'hotel_list.html', {'chambres': chambres,'hotels': hotels})

def hotel_create(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hôtel ajouté avec succès!")
            return redirect(reverse('hotel_list'))
    else:
        form = HotelForm()
    return render(request, 'hotel_form.html', {'form': form})

def hotel_update(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, "Hôtel mis à jour avec succès!")
            return redirect(reverse('hotel_list'))
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'hotel_form.html', {'form': form})

def hotel_delete(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    hotel.delete()
    messages.success(request, "Hôtel supprimé avec succès!")
    return redirect(reverse('hotel_list'))

def hotel_detail(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotel_detail.html', {'hotel': hotel})

# Vues pour gérer la Chambre

def chambre_list(request):
    chambres = Chambre.objects.select_related('hotel').prefetch_related('photos').all()
    print(chambres)  # Debug : Afficher dans la console
    return render(request, 'chambre_list.html', {'chambres': chambres})



def chambre_create(request):
    if request.method == 'POST':
        form = ChambreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Chambre ajoutée avec succès!")
            return redirect(reverse('chambre_list'))
    else:
        form = ChambreForm()
    return render(request, 'chambre_form.html', {'form': form})

def chambre_update(request, pk):
    chambre = get_object_or_404(Chambre, pk=pk)
    if request.method == 'POST':
        form = ChambreForm(request.POST, instance=chambre)
        if form.is_valid():
            form.save()
            messages.success(request, "Chambre mise à jour avec succès!")
            return redirect(reverse('chambre_list'))
    else:
        form = ChambreForm(instance=chambre)
    return render(request, 'chambre_form.html', {'form': form})

def chambre_delete(request, pk):
    chambre = get_object_or_404(Chambre, pk=pk)
    chambre.delete()
    messages.success(request, "Chambre supprimée avec succès!")
    return redirect(reverse('chambre_list'))

def chambre_detail(request, pk):
    chambre = get_object_or_404(Chambre, pk=pk)
    return render(request, 'chambre_detail.html', {'chambre': chambre})

# Vues pour gérer les Photos de Chambre

def photo_chambre_create(request, chambre_pk):
    chambre = Chambre.objects.get(pk=chambre_pk)
    if request.method == 'POST':
        form = PhotoChambreForm(request.POST, request.FILES)
        if form.is_valid():
            photo_chambre = form.save(commit=False)
            photo_chambre.chambre = chambre
            photo_chambre.save()
            messages.success(request, "Photo ajoutée avec succès!")
            return redirect(reverse('chambre_detail', args=[chambre_pk]))
    else:
        form = PhotoChambreForm()
    return render(request, 'photo_chambre_form.html', {'form': form, 'chambre': chambre})

def photo_chambre_delete(request, pk):
    photo_chambre = get_object_or_404(PhotoChambre, pk=pk)
    chambre_pk = photo_chambre.chambre.pk
    photo_chambre.delete()
    messages.success(request, "Photo supprimée avec succès!")
    return redirect(reverse('chambre_detail', args=[chambre_pk]))

# Vues pour gérer la Reservation

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Réservation effectuée avec succès!")
            return redirect(reverse('reservation_list'))
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, "Réservation mise à jour avec succès!")
            return redirect(reverse('reservation_list'))
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    messages.success(request, "Réservation supprimée avec succès!")
    return redirect(reverse('reservation_list'))

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})
