# Generated by Django 3.1 on 2023-10-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=50)),
                ('blog', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('noblog', models.IntegerField()),
            ],
        ),
    ]
