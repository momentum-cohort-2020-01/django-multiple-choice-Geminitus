# Generated by Django 3.0.4 on 2020-03-16 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChunkCascade', '0004_auto_20200316_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='favorited',
            field=models.BooleanField(default=False),
        ),
    ]