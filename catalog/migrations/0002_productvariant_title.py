# Generated by Django 2.0.5 on 2018-05-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='title',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
