# Generated by Django 4.1.5 on 2023-01-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0044_profile_automatically_verifiable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='automatically_verifiable',
            field=models.BooleanField(blank=True, default=True, verbose_name='tells if someone is automatically verifiable, set to true if it fails'),
        ),
    ]
