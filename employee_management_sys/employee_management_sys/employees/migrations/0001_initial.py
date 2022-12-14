# Generated by Django 4.1.3 on 2022-11-29 09:40

import django.core.validators
from django.db import migrations, models
import employee_management_sys.base.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40, validators=[employee_management_sys.base.validators.validate_only_letters, django.core.validators.MinLengthValidator(2)], verbose_name='First Name')),
                ('last_name', models.CharField(max_length=40, validators=[employee_management_sys.base.validators.validate_only_letters, django.core.validators.MinLengthValidator(2)], verbose_name='Last Name')),
                ('cell', models.CharField(blank=True, choices=[('C01', 'C01'), ('C02', 'C02'), ('C03', 'C03'), ('C04', 'C04'), ('C05', 'C05')], default='Not Assigned', max_length=50)),
                ('emp_id', models.CharField(max_length=7, unique=True, verbose_name='Employee Id')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
