# Generated by Django 5.0.1 on 2024-01-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_alter_personal_info_address_alter_personal_info_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_experience',
            name='date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='work_experience',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
