# Generated by Django 3.1.6 on 2021-03-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetlist',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='budgetlist',
            name='last_updated',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='budgetlist',
            name='savings_goal',
            field=models.IntegerField(null=True),
        ),
    ]
