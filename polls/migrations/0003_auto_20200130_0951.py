# Generated by Django 3.0.2 on 2020-01-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200129_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='Horas',
            field=models.IntegerField(max_length=100),
        ),
    ]