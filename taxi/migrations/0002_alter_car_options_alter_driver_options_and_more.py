# Generated by Django 5.0.4 on 2024-04-18 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('manufacturer',)},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ('username',)},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='car',
            name='drivers',
            field=models.ManyToManyField(related_name='cars', to=settings.AUTH_USER_MODEL),
        ),
    ]
