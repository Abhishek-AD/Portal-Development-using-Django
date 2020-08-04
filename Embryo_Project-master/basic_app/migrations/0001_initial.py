# Generated by Django 2.2.5 on 2020-02-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_ID', models.IntegerField(unique=True)),
                ('speaker', models.CharField(max_length=264)),
                ('discipline', models.CharField(max_length=264)),
                ('date', models.DateField()),
                ('topic', models.CharField(max_length=264)),
                ('abstract', models.TextField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
