# Generated by Django 4.1.4 on 2023-01-02 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_text_text_unique_text_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='slug',
        ),
    ]
