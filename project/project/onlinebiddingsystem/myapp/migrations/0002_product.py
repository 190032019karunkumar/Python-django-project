# Generated by Django 3.2.2 on 2021-05-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('owner', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
