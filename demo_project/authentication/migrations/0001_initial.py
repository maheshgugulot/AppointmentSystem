# Generated by Django 4.2.2 on 2023-06-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
