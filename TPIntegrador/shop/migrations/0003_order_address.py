# Generated by Django 3.2.4 on 2021-07-05 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
