

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_sepet_urun'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='garanti',
            field=models.IntegerField(default=0, verbose_name='Garanti Durumu (Varsa ay olarak yoksa 0)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urun',
            name='kargoucreti',
            field=models.IntegerField(default=0, verbose_name='Kargo Ücreti'),
            preserve_default=False,
        ),
    ]
