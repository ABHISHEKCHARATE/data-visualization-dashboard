# Generated by Django 5.1.7 on 2025-03-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
