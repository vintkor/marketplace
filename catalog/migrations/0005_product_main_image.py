# Generated by Django 2.0.5 on 2018-05-21 21:32

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default=' ', upload_to=catalog.models.set_product_image_name),
            preserve_default=False,
        ),
    ]
