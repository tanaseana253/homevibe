# Generated by Django 4.2.2 on 2023-07-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homevibe', '0004_alter_photo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='static/images/rooms'),
        ),
    ]
