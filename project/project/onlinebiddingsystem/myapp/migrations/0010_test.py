# Generated by Django 3.2.2 on 2021-05-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_bid_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='pics')),
                ('story', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'test',
            },
        ),
    ]
