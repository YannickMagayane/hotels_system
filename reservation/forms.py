from django import forms
from .models import Hotel, Chambre, PhotoChambre, Reservation

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['nom', 'adresse', 'telephone', 'description']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'adresse': forms.Textarea(attrs={'class': 'w-full p-2 border text-black rounded-md', 'rows': 3}),
            'telephone': forms.TextInput(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border text-black rounded-md', 'rows': 3}),
        }

class ChambreForm(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = ['hotel', 'numero', 'type', 'prix', 'disponible']
        widgets = {
            'hotel': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'numero': forms.TextInput(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'type': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'prix': forms.NumberInput(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'w-6 h-6'}),
        }

class PhotoChambreForm(forms.ModelForm):
    class Meta:
        model = PhotoChambre
        fields = ['chambre', 'image']
        widgets = {
            'chambre': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'chambre', 'date_debut', 'date_fin', 'statut']
        widgets = {
            'user': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'chambre': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
            'date_debut': forms.DateInput(attrs={'class': 'w-full p-2 border text-black rounded-md', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'w-full p-2 border text-black rounded-md', 'type': 'date'}),
            'statut': forms.Select(attrs={'class': 'w-full p-2 border text-black rounded-md'}),
        }
