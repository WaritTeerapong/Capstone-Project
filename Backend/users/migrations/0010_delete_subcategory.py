# Generated by Django 4.2.10 on 2024-05-07 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_category_categoryid_alter_place_placeid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]