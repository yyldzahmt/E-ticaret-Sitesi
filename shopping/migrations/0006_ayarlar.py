

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_sepet_toplamfiyat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ayarlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteadi', models.CharField(max_length=150, verbose_name='Site Adı')),
                ('facebookadresi', models.CharField(max_length=150, verbose_name='Facebook Adresi')),
                ('twitteradresi', models.CharField(max_length=150, verbose_name='Twitter Adresi')),
                ('instagramadresi', models.CharField(max_length=150, verbose_name='Instagram Adresi')),
                ('logo', models.FileField(blank=True, null=True, upload_to='', verbose_name='Logo')),
                ('footeralani', models.CharField(max_length=250, verbose_name='Footerdeki Yazı Alanı')),
            ],
        ),
    ]
