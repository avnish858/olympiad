# Generated by Django 3.0.3 on 2020-08-01 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0014_auto_20200801_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='final_generalolym',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='generalolym',
            field=models.BooleanField(default=False, null=True),
        ),
    ]