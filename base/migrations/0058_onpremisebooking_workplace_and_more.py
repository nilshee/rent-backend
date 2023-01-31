# Generated by Django 4.1.5 on 2023-01-28 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0057_onpremiseworkplace_displayed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='onpremisebooking',
            name='workplace',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.onpremiseworkplace'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='onpremiseworkplacestatus',
            name='workplace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='base.onpremiseworkplace'),
        ),
    ]