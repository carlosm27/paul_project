# Generated by Django 5.1.7 on 2025-03-10 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.FloatField(max_length=20)),
                ('precio', models.FloatField(max_length=20)),
            ],
        ),
    ]
