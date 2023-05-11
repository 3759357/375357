# Generated by Django 4.1.7 on 2023-05-07 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_test', '0002_remove_member_reg_date_remove_member_update_date_and_more'),
        ('food', '0003_food_food_name_alter_food_serving_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_test.member')),
            ],
        ),
    ]
