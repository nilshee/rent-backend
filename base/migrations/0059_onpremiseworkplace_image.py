# Generated by Django 4.1.5 on 2023-01-29 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0058_onpremisebooking_workplace_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onpremiseworkplace',
            name='image',
            field=models.ImageField(default='nopicture.png', upload_to=''),
        ),
    ]