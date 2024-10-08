# Generated by Django 4.2.2 on 2023-08-31 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homevibe', '0005_alter_color_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homevibe.color'),
        ),
        migrations.AddField(
            model_name='photo',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homevibe.room'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='products',
            field=models.ManyToManyField(blank=True, to='homevibe.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/product'),
        ),
    ]
