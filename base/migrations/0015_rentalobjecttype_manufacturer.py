# Generated by Django 4.1.4 on 2022-12-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_objecttypeinfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalobjecttype',
            name='manufacturer',
            field=models.CharField(default='', max_length=100),
        ),
    ]
