# Generated by Django 2.2 on 2019-10-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000000),
        ),
    ]