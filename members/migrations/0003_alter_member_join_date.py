# Generated by Django 5.1.1 on 2024-09-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_delete_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(null=True),
        ),
    ]
