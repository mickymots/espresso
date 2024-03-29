# Generated by Django 3.2 on 2021-05-04 23:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('beans_intake', '0003_alter_inventory_partial_bag_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='HullGradeIntake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_type', models.CharField(max_length=2)),
                ('intake_id', models.IntegerField()),
                ('no_of_full_bags', models.FloatField(blank=True, default=0.0, null=True)),
                ('partial_weight', models.IntegerField(blank=True, default=0, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('supervisor_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='beans_intake.employee')),
            ],
        ),migrations.RunSQL(
           'ALTER SEQUENCE hull_grade_hullgradeintake_id_seq RESTART WITH 9000000;'
        )
    ]
