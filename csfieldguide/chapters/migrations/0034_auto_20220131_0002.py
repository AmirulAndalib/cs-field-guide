# Generated by Django 3.2.8 on 2022-01-31 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0033_auto_20210805_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='chaptersection',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='chaptersectionheading',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='glossaryterm',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]