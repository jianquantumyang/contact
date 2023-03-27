# Generated by Django 4.1.5 on 2023-03-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_cuser_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='cuser',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождение'),
        ),
    ]
