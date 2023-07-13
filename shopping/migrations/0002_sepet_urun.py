

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urunadi', models.CharField(max_length=250, verbose_name='Ürün Adı')),
                ('urunaciklamasi', models.TextField(max_length=5000, verbose_name='Ürün Açıklaması')),
                ('fiyat', models.IntegerField(verbose_name='Fiyatı')),
                ('urunresmi', models.FileField(blank=True, null=True, upload_to='', verbose_name='Ürün Resmi')),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.kategoriler', verbose_name='Kategorisi')),
            ],
        ),
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adet', models.IntegerField(verbose_name='Ürünün Adeti')),
                ('sahibi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ürünün Sahibi')),
                ('urun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.urun', verbose_name='Sepetteki Ürün')),
            ],
        ),
    ]
