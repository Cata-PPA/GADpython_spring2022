# Generated by Django 4.0.4 on 2022-05-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appjob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='description_job',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='how_to_apply',
            field=models.TextField(blank=True),
        ),
    ]
