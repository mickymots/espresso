# Generated by Django 3.2 on 2021-04-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parchment_intake', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parchmentintake',
            name='marker_placed',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
