# Generated by Django 3.2.22 on 2023-10-25 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0001_initial'),
        ('DM_Head', '0002_auto_20231020_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_discription', models.TextField(blank=True, default='', null=True)),
                ('ta_file', models.FileField(default='', upload_to='work\\files')),
                ('ta_progress', models.IntegerField(default=0)),
                ('ta_allocate_date', models.DateField(null=True)),
                ('ta_start_date', models.DateField(auto_now=True, null=True)),
                ('ta_due_date', models.DateField(null=True)),
                ('ta_target', models.IntegerField(default=0)),
                ('ta_status', models.IntegerField(default=0)),
                ('ta_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='clienttask_register',
            name='task_total_progress',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tad_collect_date', models.DateField(auto_now=True, null=True)),
                ('tad_title', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('tad_discription', models.TextField(blank=True, default='', null=True)),
                ('tad_file', models.JSONField(default=list)),
                ('tad_target', models.IntegerField(default=0)),
                ('tad_status', models.IntegerField(default=0)),
                ('tad_taskAssignId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.taskassign')),
            ],
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_taskId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clienttask_register'),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_workAssignId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workassign'),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_workerId',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration_Login.employeeregister_details'),
        ),
    ]
