# Generated by Django 4.2.7 on 2023-12-05 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestant', '0003_alter_contestant_city_alter_contestant_hobbies_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='city',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='hobbies',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='job',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='nationality',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
        migrations.AlterField(
            model_name='musicstyle',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='musicstyle',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]