import requests
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def index(request):
    kategoriler = Kategoriler.objects.all()
    ayarlar = Ayarlar.objects.get(id=1)
    if request.user.is_authenticated:
        sepet = Sepet.objects.filter(sahibi=request.user)
        sepettutari = 0
        for u in sepet:
            sepettutari += u.toplamfiyat

    else:
        sepet = list()
        sepettutari = 0

    context = {
        "title": "Ana Sayfa | {}".format(ayarlar.siteadi),
        "kategoriler": kategoriler,
        "sepet": sepet,
        "sepettutari": sepettutari,
        "ayarlar":ayarlar
    }

    return render(request, "index.html", context)


def kategori(request, kategoriid):
    try:
        kategoribilgi = Kategoriler.objects.get(id=kategoriid)
        ayarlar = Ayarlar.objects.get(id=1)
        if request.user.is_authenticated:
            sepet = Sepet.objects.filter(sahibi=request.user)
            sepettutari = 0
            for u in sepet:
                sepettutari += u.toplamfiyat
        else:
            sepet = list()
            sepettutari = 0
        urunler = Urun.objects.filter(kategori=kategoribilgi.id)
        context = {
            "title": "{} Kategorisindeki Ürünler Listeleniyor | {}".format(kategoribilgi.kategoriadi,ayarlar.siteadi),
            "urunler": urunler,
            "kategoribilgileri": kategoribilgi,
            "sepet": sepet,
            "sepettutari": sepettutari,
            "ayarlar":ayarlar
        }
        return render(request, "urunler.html", context)
    except:
        return redirect("index")



def urun(request, urunid):
    try:
        urun = Urun.objects.get(id=urunid)
        ayarlar = Ayarlar.objects.get(id=1)
        if request.user.is_authenticated:
            sepet = Sepet.objects.filter(sahibi=request.user)
            sepettutari = 0
            for u in sepet:
                sepettutari += u.toplamfiyat
        else:
            sepet = list()
            sepettutari = 0
        if request.method == "POST":
            adet = int(request.POST['adet'])
            if adet > 0 and adet <= 15:
                sepeteekle = Sepet(adet=adet, urun=urun, sahibi=request.user, toplamfiyat=urun.fiyat * adet)
                sepeteekle.save()
                messages.success(request, "Ürün sepete eklendi.")
                return redirect("/urun/"+str(urunid))

        context = {
            "title": "{} ürününün detayları | {}".format(urun.urunadi,ayarlar.siteadi),
            "urun": urun,
            "sepet": sepet,
            "sepettutari": sepettutari,
            "ayarlar":ayarlar
        }
        return render(request, "urun.html", context)
    except:
        return redirect("index")


def giris(request):
    form = GirisYap()
    if request.method == "POST":
        form = GirisYap(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("eposta")
            sifre = form.cleaned_data.get("sifre")
            kullanici = authenticate(username=email, password=sifre)

            if kullanici is None:
                messages.info(request, "E-posta veya şifre hatalı")
            else:
                messages.success(request, "Giriş yapıldı.")
                login(request, kullanici)
                return redirect("index")
    ayarlar = Ayarlar.objects.get(id=1)
    context = {
        "title": "Giriş Yap | {}".format(ayarlar.siteadi),
        "form": form,
        "ayarlar":ayarlar
    }
    return render(request, "giris.html", context)


def cikis(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def kayit(request):
    if request.user.is_authenticated:
        return redirect(request, "index")
    ayarlar = Ayarlar.objects.get(id=1)
    form = KayitOl()
    if request.method == "POST":
        form = KayitOl(request.POST)
        if form.is_valid():
            sifre = form.cleaned_data.get("sifre")
            adi = form.cleaned_data.get("adi")
            soyadi = form.cleaned_data.get("soyadi")
            eposta = form.cleaned_data.get("eposta")
            adres = form.cleaned_data.get("adres")
            try:
                yenikullanici = User(username=eposta, first_name=adi, last_name=soyadi, email=eposta)
                yenikullanici.set_password(sifre)
                yenikullanici.save()
                yeniadres = Adres(adres=adres, kullanici=yenikullanici)
                yeniadres.save()
                messages.success(request, "Başarılı bir şekilde kaydınız tamamlanmıştır.")
                login(request, yenikullanici)
                return redirect("index")
            except:
                messages.warning(request, "Bu bilgilere sahip bir üye zaten var.")

    context = {
        "title": "Kayıt Ol | {}".format(ayarlar.siteadi),
        "form": form,
        "ayarlar":ayarlar
    }
    return render(request, "kayitol.html", context)

def sepetibosalt(request):
    if request.user.is_authenticated:
        Sepet.objects.filter(sahibi=request.user).delete()
    messages.success(request,"Sepet Boşaltıldı.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def sepettensil(request,id):
    if request.user.is_authenticated:
        urun = Sepet.objects.get(id=id)
        if urun.sahibi==request.user:
            urun.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))