# Generated by Django 4.1.7 on 2023-04-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="region",
            field=models.CharField(default="1", max_length=200),
            preserve_default=False,
        ),
    ]
