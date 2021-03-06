# Generated by Django 2.0.2 on 2018-03-04 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('initials', models.CharField(max_length=2, verbose_name='initials')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.Country', verbose_name='country')),
            ],
        ),
    ]
