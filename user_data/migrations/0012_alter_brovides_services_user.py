# Generated by Django 5.0.4 on 2024-09-25 13:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0011_brovides_services_indebtedness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brovides_services',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]