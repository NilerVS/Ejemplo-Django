# Generated by Django 4.2.7 on 2023-11-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('apellidoPaterno', models.CharField(max_length=100, verbose_name='apellidop')),
                ('apellidoMaterno', models.CharField(max_length=100, verbose_name='apellidom')),
            ],
        ),
    ]