# Generated by Django 4.2.10 on 2024-04-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_item_image_alter_request_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='dateFound',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='dateLost',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='dateRequest',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
