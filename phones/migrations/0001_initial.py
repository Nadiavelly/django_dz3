# Generated by Django 4.0.2 on 2022-08-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=300)),
                ('realise_date', models.CharField(max_length=100)),
                ('lte_exists', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
