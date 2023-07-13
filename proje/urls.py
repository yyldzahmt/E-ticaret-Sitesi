"""proje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopping import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('kategori/<int:kategoriid>',views.kategori),
    path('urun/<int:urunid>',views.urun),
    path('giris/',views.giris),
    path('kayit/',views.kayit),
    path('cikis/',views.cikis),
    path('sepetibosalt/',views.sepetibosalt),
    path('sepettensil/<int:id>',views.sepettensil)


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)