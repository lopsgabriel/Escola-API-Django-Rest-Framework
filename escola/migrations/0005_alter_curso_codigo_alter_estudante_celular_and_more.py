# Generated by Django 5.1.2 on 2024-10-25 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='codigo',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='celular',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='estudante',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
    ]
