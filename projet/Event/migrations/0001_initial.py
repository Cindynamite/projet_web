# Generated by Django 3.0.dev20190429122017 on 2019-05-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEvent', models.CharField(max_length=100)),
                ('idAsso', models.IntegerField()),
                ('lieu', models.CharField(max_length=100)),
                ('nbBenevole', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('dateDebut', models.DateTimeField(verbose_name='Date de début')),
                ('dateFin', models.DateTimeField(verbose_name='Date de fin')),
            ],
        ),
    ]
