# Generated by Django 4.1.7 on 2023-04-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("member_id", models.CharField(db_column="member_id", max_length=50)),
                ("passwd", models.CharField(db_column="passwd", max_length=50)),
                ("name", models.CharField(db_column="name", max_length=50)),
                (
                    "email",
                    models.CharField(blank=True, db_column="email", max_length=50),
                ),
                (
                    "usage_flag",
                    models.CharField(
                        db_column="usage_flag", default="y", max_length=10
                    ),
                ),
                (
                    "reg_date",
                    models.DateTimeField(auto_now_add=True, db_column="reg_date"),
                ),
                (
                    "update_date",
                    models.DateTimeField(auto_now_add=True, db_column="update_date"),
                ),
            ],
            options={
                "db_table": "member",
            },
        ),
    ]
