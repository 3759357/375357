# Generated by Django 4.1.7 on 2023-04-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "serving_size",
                    models.CharField(db_column="serving_size", max_length=50),
                ),
                ("calories", models.IntegerField(db_column="calories", default=0)),
                ("carbon", models.IntegerField(db_column="carbon", default=0)),
                ("protein", models.IntegerField(db_column="protein", default=0)),
                ("fat", models.IntegerField(db_column="fat", default=0)),
                (
                    "cholesterol",
                    models.IntegerField(db_column="cholesterol", default=0),
                ),
            ],
            options={
                "db_table": "food",
            },
        ),
        migrations.DeleteModel(
            name="Answer",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
