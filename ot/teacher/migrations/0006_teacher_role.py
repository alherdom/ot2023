# Generated by Django 4.2.7 on 2023-12-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0005_teacher_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="role",
            field=models.CharField(default="Concursante", max_length=20),
            preserve_default=False,
        ),
    ]
