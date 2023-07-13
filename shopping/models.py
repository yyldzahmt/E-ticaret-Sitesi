from django.db import models

class Kategoriler(models.Model):
    kategoriadi = models.CharField(max_length=250,verbose_name="Kategori Adı")
    kategoriaciklamasi = models.TextField(max_length=5000,verbose_name="Kategori Açıklaması")
    kategoriresmi = models.FileField(blank=True,null=True,verbose_name="Kategori Resmi")

    def __str__(self):
        return self.kategoriadi

class Urun(models.Model):
    urunadi = models.CharField(max_length=250,verbose_name="Ürün Adı")
    urunaciklamasi = models.TextField(max_length=5000,verbose_name="Ürün Açıklaması")
    fiyat = models.IntegerField(verbose_name="Fiyatı")
    kategori = models.ForeignKey("shopping.Kategoriler",verbose_name="Kategorisi",on_delete=models.CASCADE)
    urunresmi = models.FileField(blank=True,null=True,verbose_name="Ürün Resmi")
    kargoucreti = models.IntegerField(verbose_name="Kargo Ücreti")
    garanti = models.IntegerField(verbose_name="Garanti Durumu (Varsa ay olarak yoksa 0)")

    def __str__(self):
        return self.urunadi


class Sepet(models.Model):
    urun = models.ForeignKey("shopping.Urun",verbose_name="Sepetteki Ürün",on_delete=models.CASCADE)
    sahibi = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Ürünün Sahibi")
    adet = models.IntegerField(verbose_name="Ürünün Adeti")
    toplamfiyat = models.IntegerField(verbose_name="Toplam Fiyat")

    def __str__(self):
        return self.urun.urunadi

class Adres(models.Model):
    adres = models.TextField(max_length=1000,verbose_name="Adres")
    kullanici = models.ForeignKey("auth.User",verbose_name="Kullanıcı",on_delete=models.CASCADE)

class Ayarlar(models.Model):
    siteadi = models.CharField(max_length=150,verbose_name="Site Adı")
    facebookadresi = models.CharField(max_length=150,verbose_name="Facebook Adresi")
    twitteradresi = models.CharField(max_length=150, verbose_name="Twitter Adresi")
    instagramadresi = models.CharField(max_length=150, verbose_name="Instagram Adresi")
    logo = models.FileField(blank=True,null=True,verbose_name="Logo")
    footeralani = models.CharField(max_length=250,verbose_name="Footerdeki Yazı Alanı")