# Generated by Django 4.1.7 on 2023-03-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='link',
        ),
        migrations.AddField(
            model_name='job',
            name='job_role',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
