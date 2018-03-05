# Generated by Django 2.0.2 on 2018-03-04 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('zipcode', models.CharField(blank=True, max_length=8, null=True, verbose_name='zipcode')),
                ('ibge', models.CharField(blank=True, max_length=10, null=True, verbose_name='ibge')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='updated at')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.State', verbose_name='state')),
            ],
        ),
    ]