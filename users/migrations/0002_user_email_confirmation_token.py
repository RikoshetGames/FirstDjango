# Generated by Django 5.0 on 2024-01-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmation_token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]