# Generated by Django 4.1.3 on 2022-12-10 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cells', '0005_alter_cells_cell_name'),
        ('orders', '0002_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cell',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cells.cells'),
        ),
    ]
