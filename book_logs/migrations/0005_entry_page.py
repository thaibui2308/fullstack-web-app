# Generated by Django 3.2.3 on 2021-05-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_logs', '0004_book_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='page',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
