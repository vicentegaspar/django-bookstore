# Generated by Django 4.1.5 on 2023-01-23 22:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category",
            old_name="price",
            new_name="description",
        ),
    ]
