# Generated by Django 4.2.7 on 2023-11-16 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Languageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
