# Generated by Django 4.2.7 on 2023-11-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0007_usermodel_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usermodel",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
