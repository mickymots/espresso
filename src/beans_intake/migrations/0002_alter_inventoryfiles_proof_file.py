# Generated by Django 3.2 on 2021-04-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beans_intake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryfiles',
            name='proof_file',
            field=models.FileField(blank=True, null=True, upload_to='inventory-files'),
        ),
    ]