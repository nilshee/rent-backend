# Generated by Django 4.1.4 on 2023-01-02 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_text_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
