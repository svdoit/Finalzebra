# Generated by Django 3.1.3 on 2020-11-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zebraapp', '0007_auto_20201119_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myitem',
            name='itemDate',
            field=models.DateField(verbose_name='date published'),
        ),
    ]