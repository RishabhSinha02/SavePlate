# Generated by Django 4.1.5 on 2023-01-20 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_donations_donated_at_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/donations/images/'),
        ),
    ]