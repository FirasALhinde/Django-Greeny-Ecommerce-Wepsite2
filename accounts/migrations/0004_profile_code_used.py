# Generated by Django 3.2 on 2023-01-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code_used',
            field=models.BooleanField(default=False, verbose_name='Code Used'),
        ),
    ]
