# Generated by Django 4.2.2 on 2023-08-29 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homevibe', '0003_remove_room_room_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
