# Generated by Django 2.2.5 on 2020-03-13 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceperson',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='resourceperson',
            name='department',
            field=models.CharField(blank=True, choices=[('BIO', 'Biological Sciences'), ('CHE', 'Chemical'), ('CHEM', 'Chemistry'), ('CE', 'Civil'), ('CS', 'Computer Science'), ('EEE', 'Electical and Electronics'), ('ECON', 'Economics and Finances'), ('HSS', 'Humanities and Social Sciences'), ('MATH', 'Mathematics'), ('ME', 'Mechanical'), ('PHA', 'Pharmacy'), ('PHY', 'Physics'), ('BITS', 'Other')], max_length=264),
        ),
        migrations.AlterField(
            model_name='resourceperson',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]