# Generated by Django 4.2.3 on 2023-11-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_hr', '0003_candidatedetails_data_added_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='Mobile_no',
            field=models.IntegerField(),
        ),
    ]
