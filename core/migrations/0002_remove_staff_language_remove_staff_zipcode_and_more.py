# Generated by Django 5.1.5 on 2025-02-05 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='language',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='zipcode',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Zipcode',
        ),
    ]
