# Generated by Django 3.2 on 2021-04-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parchment_intake', '0002_parchmentintake_marker_placed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parchmentintake',
            name='marker_placed',
            field=models.BooleanField(default=False),
        ),
    ]