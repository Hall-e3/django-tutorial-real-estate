# Generated by Django 3.2.7 on 2022-11-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20221031_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='top_seller',
            field=models.BooleanField(default=False, help_text='Are you a top seller?', verbose_name='Top Seller'),
        ),
    ]