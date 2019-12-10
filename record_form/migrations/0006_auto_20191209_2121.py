# Generated by Django 2.2.7 on 2019-12-09 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record_form', '0005_personinfo_passport_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
