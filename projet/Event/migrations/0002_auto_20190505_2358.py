# Generated by Django 3.0.dev20190429122017 on 2019-05-05 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['id'], 'verbose_name': 'evenement'},
        ),
    ]
