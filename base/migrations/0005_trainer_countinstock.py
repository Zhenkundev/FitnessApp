# Generated by Django 3.1.4 on 2022-02-26 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220224_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='countInStock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
