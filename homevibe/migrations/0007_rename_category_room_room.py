# Generated by Django 4.2.2 on 2023-08-31 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homevibe', '0006_photo_color_photo_room_alter_photo_products_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='category',
            new_name='room',
        ),
    ]
