# Generated by Django 2.2 on 2019-10-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20191025_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesdata',
            name='price',
            field=models.CharField(max_length=200),
        ),
    ]
