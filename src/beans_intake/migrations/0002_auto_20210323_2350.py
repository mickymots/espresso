# Generated by Django 3.1.7 on 2021-03-23 23:50

from django.db import migrations, models
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('beans_intake', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intake',
            name='representative_name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='intake',
            name='representative_signature',
            field=jsignature.fields.JSignatureField(blank=True, null=True),
        ),
    ]
