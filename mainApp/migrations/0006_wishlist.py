# Generated by Django 4.1.2 on 2023-10-13 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
    ]
