# Generated by Django 3.1.7 on 2021-03-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beans_intake', '0003_auto_20210324_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='refloat',
            name='floated',
            field=models.BooleanField(default=False),
        ),
    ]
