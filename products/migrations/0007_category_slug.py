# Generated by Django 4.1.5 on 2023-02-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
