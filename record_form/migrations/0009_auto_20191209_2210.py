# Generated by Django 2.2.7 on 2019-12-09 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record_form', '0008_auto_20191209_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personinfo',
            name='creator',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]