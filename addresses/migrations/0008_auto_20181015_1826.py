# Generated by Django 2.1.2 on 2018-10-15 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0007_auto_20181015_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='country',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]