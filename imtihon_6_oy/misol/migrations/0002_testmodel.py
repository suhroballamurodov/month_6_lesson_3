# Generated by Django 4.2.7 on 2023-11-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savol', models.TextField(default="13 + 24 nechchi bo'ladi ?")),
                ('a', models.IntegerField(default=27)),
                ('b', models.IntegerField(default=56)),
                ('c', models.IntegerField(default=68)),
            ],
        ),
    ]