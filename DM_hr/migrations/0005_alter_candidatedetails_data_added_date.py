# Generated by Django 4.2.3 on 2023-11-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_hr', '0004_alter_candidatedetails_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedetails',
            name='data_added_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
