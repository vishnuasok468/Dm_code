# Generated by Django 4.2.3 on 2023-11-02 10:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_hr', '0005_alter_candidatedetails_data_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='Mobile_no',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999999), django.core.validators.MinValueValidator(100000000000)]),
        ),
    ]