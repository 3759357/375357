# Generated by Django 4.1.7 on 2023-05-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0002_remove_member_reg_date_remove_member_update_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.IntegerField(db_column='gender', default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='purpose',
            field=models.IntegerField(db_column='purpose', default=0),
        ),
    ]