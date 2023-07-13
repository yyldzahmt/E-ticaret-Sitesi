

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_adres'),
    ]

    operations = [
        migrations.AddField(
            model_name='sepet',
            name='toplamfiyat',
            field=models.IntegerField(default=0, verbose_name='Toplam Fiyat'),
            preserve_default=False,
        ),
    ]
