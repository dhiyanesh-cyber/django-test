# Generated by Django 4.2.5 on 2023-09-25 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("getDoctors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="id",
            field=models.AutoField(db_column="id", primary_key=True, serialize=False),
        ),
    ]
