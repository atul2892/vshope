# Generated by Django 4.1.2 on 2023-10-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_buyer_pic_alter_product_pic1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic1', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('pic2', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('pic3', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('pic4', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('pic5', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
            ],
        ),
    ]
