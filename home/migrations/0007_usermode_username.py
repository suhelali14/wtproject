# Generated by Django 4.2.4 on 2023-08-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_profile_usermode'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermode',
            name='username',
            field=models.CharField(default='shakil', max_length=100),
            preserve_default=False,
        ),
    ]