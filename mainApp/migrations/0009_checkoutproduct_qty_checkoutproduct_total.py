# Generated by Django 4.1.2 on 2023-10-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_checkout_checkoutproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproduct',
            name='qty',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='checkoutproduct',
            name='total',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
