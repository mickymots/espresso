# Generated by Django 3.2 on 2021-04-21 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beans_intake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
