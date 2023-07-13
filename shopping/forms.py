from django import forms
from django.contrib import messages


class GirisYap(forms.Form):
    eposta = forms.EmailField(max_length=25, label="E-Posta", required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'E-Posta Adresi'}))
    sifre = forms.CharField(max_length=50, label="Şifre", widget=forms.PasswordInput(attrs={'placeholder':'Şifreniz'}), required=True)

    def clean(self):
        eposta = self.cleaned_data.get("eposta")
        sifre = self.cleaned_data.get("sifre")

        values = {
            "eposta": eposta,
            "sifre": sifre
        }
        return values

class KayitOl(forms.Form):
    sifre = forms.CharField(max_length=50, label="Şifre", widget=forms.PasswordInput(attrs={'placeholder': 'Şifreniz'}),
                            required=True)
    adi = forms.CharField(max_length=25, label="Adınız", required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Adınız'}))
    soyadi = forms.CharField(max_length=25, label="Soyadınız", required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Soyadı'}))
    eposta = forms.EmailField(max_length=25, label="E-Posta", required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'E-Posta Adresiniz'}))
    adres = forms.CharField(max_length=500, label="Adresiniz", required=True,
                             widget=forms.Textarea(attrs={'placeholder': 'Adresiniz'}))

    def clean(self):
        sifre = self.cleaned_data.get("sifre")
        adi = self.cleaned_data.get("adi")
        soyadi = self.cleaned_data.get("soyadi")
        eposta = self.cleaned_data.get("eposta")
        adres = self.cleaned_data.get("adres")

        values = {
            "sifre":sifre,
            "adi":adi,
            "soyadi":soyadi,
            "eposta":eposta,
            "adres":adres
        }
        return values