# Generated by Django 4.1.2 on 2022-10-17 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
            ],
        ),
    ]
