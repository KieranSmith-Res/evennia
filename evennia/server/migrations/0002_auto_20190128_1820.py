# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 18:20

import pickle
from django.db import migrations, models
import evennia.utils.picklefield
from evennia.utils.utils import to_bytes

def migrate_serverconf(apps, schema_editor):
    """
    Move server conf from a custom binary field into a PickleObjectField
    """
    ServerConfig = apps.get_model("server", "ServerConfig")
    for conf in ServerConfig.objects.all():
        value = pickle.loads(utils.to_bytes(conf.db_value))
        conf.db_value2 = value
        conf.save()


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverconfig',
            name='db_value2',
            field=evennia.utils.picklefield.PickledObjectField(help_text='The data returned when the config value is accessed. Must be written as a Python literal if editing through the admin interface. Attribute values which are not Python literals cannot be edited through the admin interface.', null=True, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='serverconfig',
            name='db_value',
            field=models.BinaryField(blank=True),
        ),
        # migrate data
        migrations.RunPython(migrate_serverconf, migrations.RunPython.noop),


    ]
