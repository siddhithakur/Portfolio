# Generated by Django 3.0.4 on 2020-03-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200329_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
