# Generated by Django 2.1.7 on 2019-04-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountsystem', '0005_auto_20190430_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expend',
            name='people',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='income',
            name='people',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(max_length=8),
        ),
    ]