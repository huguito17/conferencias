# Generated by Django 3.2.3 on 2021-06-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0004_auto_20210629_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencista',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='conferencistas'),
        ),
    ]