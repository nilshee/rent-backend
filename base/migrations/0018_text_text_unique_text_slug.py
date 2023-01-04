# Generated by Django 4.1.4 on 2023-01-02 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rentalobjecttype_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'texts',
            },
        ),
        migrations.AddConstraint(
            model_name='text',
            constraint=models.UniqueConstraint(fields=('name',), name='Unique_text_slug'),
        ),
    ]
