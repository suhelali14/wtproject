# Generated by Django 4.2.4 on 2023-08-19 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_cartproduct_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='phone',
            field=models.TextField(default=7558436263),
            preserve_default=False,
        ),
    ]