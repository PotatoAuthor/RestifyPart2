# Generated by Django 3.2.12 on 2023-03-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customuser_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_host',
            field=models.BooleanField(default=False),
        ),
    ]
