# Generated by Django 4.1.5 on 2023-01-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetials',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userdetials',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]