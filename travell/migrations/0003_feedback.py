# Generated by Django 3.1.1 on 2020-09-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travell', '0002_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
