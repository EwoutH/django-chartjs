# Generated by Django 2.2.2 on 2019-06-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('reading', models.IntegerField()),
            ],
            options={
                'ordering': ('-date', 'name'),
            },
        ),
    ]
