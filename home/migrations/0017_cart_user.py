# Generated by Django 4.2.4 on 2023-08-15 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_cart_cloth_alter_cart_electronic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.CharField(default='suhelali', max_length=100),
            preserve_default=False,
        ),
    ]
