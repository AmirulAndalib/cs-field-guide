# Generated by Django 3.2.8 on 2022-01-31 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interactives', '0017_merge_0015_auto_20210805_0142_0016_auto_20191129_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactive',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]