# Generated by Django 3.0.4 on 2020-03-15 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc',
            field=models.FileField(upload_to='docs'),
        ),
    ]