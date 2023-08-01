# Generated by Django 4.2.3 on 2023-08-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(blank=True, max_length=100, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('esal', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
