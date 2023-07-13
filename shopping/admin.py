from django.contrib import admin
from .models import Kategoriler,Urun,Sepet,Adres,Ayarlar
@admin.register(Kategoriler)
class KategorilerAdmin(admin.ModelAdmin):
    list_display = ["kategoriadi"]
    class Meta:
        model = Kategoriler

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ["urunadi"]
    class Meta:
        model = Urun

@admin.register(Sepet)
class SepetAdmin(admin.ModelAdmin):
    list_display = ["urun"]
    class Meta:
        model = Sepet

@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ["adres"]
    class Meta:
        model = Adres

@admin.register(Ayarlar)
class AyarlarAdmin(admin.ModelAdmin):
    list_display = ["siteadi"]
    class Meta:
        model = Ayarlar