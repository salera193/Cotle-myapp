# Generated by Django 3.0.3 on 2020-05-29 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cotle', '0004_accept_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='accept',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='apply',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
