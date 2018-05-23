# Generated by Django 2.0.5 on 2018-05-23 20:39

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='image',
            field=models.ImageField(default=' ', upload_to=catalog.models.set_product_image_name),
            preserve_default=False,
        ),
    ]
