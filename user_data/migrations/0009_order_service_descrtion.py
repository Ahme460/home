# Generated by Django 5.0.4 on 2024-09-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0008_alter_cuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_service',
            name='descrtion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]