# Generated by Django 3.1.6 on 2021-03-10 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20210309_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='type',
            field=models.CharField(choices=[('Payment', 'Payment'), ('Income', 'Income')], default='Payment', max_length=26, null=True),
        ),
    ]