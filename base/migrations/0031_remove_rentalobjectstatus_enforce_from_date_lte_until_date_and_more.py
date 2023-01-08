# Generated by Django 4.1.4 on 2023-01-07 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_rentalobjectstatus_enforce_from_date_lte_until_date'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='rentalobjectstatus',
            name='enforce_from_date_lte_until_date',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='canceled',
        ),
        migrations.AlterField(
            model_name='rental',
            name='handed_out_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddConstraint(
            model_name='rental',
            constraint=models.CheckConstraint(check=models.Q(('handed_out_at__lte', models.F('received_back_at'))), name='rental_handed_out_lte_received_date'),
        ),
        migrations.AddConstraint(
            model_name='rentalobjectstatus',
            constraint=models.CheckConstraint(check=models.Q(('from_date__lte', models.F('until_date'))), name='object_status_enforce_from_date_lte_until_date'),
        ),
        migrations.AddConstraint(
            model_name='reservation',
            constraint=models.CheckConstraint(check=models.Q(('reserved_from__lte', models.F('reserved_until'))), name='reservation_reserved_from_date_lte_reserved_until'),
        ),
    ]
