# Generated by Django 3.2.5 on 2021-07-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whattime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecheck',
            name='hours',
            field=models.IntegerField(help_text='Enter hours'),
        ),
        migrations.AlterField(
            model_name='timecheck',
            name='minutes',
            field=models.IntegerField(help_text='Enter minutes'),
        ),
    ]
