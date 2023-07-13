

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoriler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoriadi', models.CharField(max_length=250, verbose_name='Kategori Adı')),
                ('kategoriaciklamasi', models.TextField(max_length=5000, verbose_name='Kategori Açıklaması')),
                ('kategoriresmi', models.FileField(blank=True, null=True, upload_to='', verbose_name='Kategori Resmi')),
            ],
        ),
    ]
