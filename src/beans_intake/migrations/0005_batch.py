# Generated by Django 3.1.7 on 2021-03-21 00:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beans_intake', '0004_ownintake_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('intake', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beans_intake.ownintake')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beans_intake.location')),
            ],
        ),
         migrations.RunSQL(
        'ALTER SEQUENCE beans_intake_batch_id_seq RESTART WITH 10000;'
    )
    ,
         migrations.RunSQL(
        'ALTER SEQUENCE beans_intake_location_id_seq RESTART WITH 10000;'
    )
    ]