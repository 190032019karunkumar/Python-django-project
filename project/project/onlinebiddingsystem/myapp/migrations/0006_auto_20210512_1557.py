# Generated by Django 3.2.2 on 2021-05-12 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210512_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='all',
            old_name='date',
            new_name='timer',
        ),
        migrations.RenameField(
            model_name='daily',
            old_name='date',
            new_name='timer',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date',
            new_name='timer',
        ),
    ]
