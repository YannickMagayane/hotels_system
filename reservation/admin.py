from django.contrib import admin
from .models import Hotel, Chambre, PhotoChambre, Reservation

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'telephone')
    search_fields = ('nom', 'adresse')
    list_filter = ('nom',)


@admin.register(Chambre)
class ChambreAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'numero', 'type', 'prix', 'disponible')
    list_filter = ('hotel', 'type', 'disponible')
    search_fields = ('numero', 'hotel__nom')


@admin.register(PhotoChambre)
class PhotoChambreAdmin(admin.ModelAdmin):
    list_display = ('chambre', 'image')
    search_fields = ('chambre__hotel__nom', 'chambre__numero')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'chambre', 'date_debut', 'date_fin', 'statut')
    list_filter = ('statut', 'date_debut', 'date_fin')
    search_fields = ('user__email', 'chambre__hotel__nom', 'chambre__numero')
    date_hierarchy = 'date_debut'
