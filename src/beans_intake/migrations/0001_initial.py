# Generated by Django 3.1.7 on 2021-03-20 19:41

from django.db import migrations, models
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnIntake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('lot_detail', models.CharField(max_length=60)),
                ('box_count', models.IntegerField()),
                ('discarded_weight', models.IntegerField()),
                ('refloated_weight', models.IntegerField()),
                ('proof_file', models.CharField(max_length=500)),
                ('signature', jsignature.fields.JSignatureField()),
            ],
        ),
         migrations.RunSQL(
        'ALTER SEQUENCE beans_intake_ownintake_id_seq RESTART WITH 10000;'
    )
    ]