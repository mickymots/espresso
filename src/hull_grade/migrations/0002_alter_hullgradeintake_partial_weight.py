# Generated by Django 3.2 on 2021-05-05 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hull_grade', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hullgradeintake',
            name='partial_weight',
            field=models.IntegerField(blank=True, choices=[(0, 'Partial Bag not picked up'), (1, 'Partial Bag picked up')], default=0, max_length=1, null=True),
        ),
    ]