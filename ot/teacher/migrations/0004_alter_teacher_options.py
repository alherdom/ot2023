# Generated by Django 4.2.7 on 2023-12-07 17:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0003_alter_teacher_slug"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="teacher",
            options={"ordering": ["id"]},
        ),
    ]