# Generated by Django 4.1.3 on 2022-12-11 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0005_alter_cells_cell_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cells',
            options={'ordering': ['cell_name']},
        ),
    ]
