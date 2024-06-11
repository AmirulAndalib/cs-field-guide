# Generated by Django 4.2.9 on 2024-02-02 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appendices', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appendix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('template', models.CharField(max_length=100)),
                ('url_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AppendixPage',
        ),
    ]