# Generated by Django 2.1.7 on 2019-06-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=20)),
                ('blog', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=20)),
                ('introduce', models.CharField(max_length=600)),
            ],
        ),
    ]
