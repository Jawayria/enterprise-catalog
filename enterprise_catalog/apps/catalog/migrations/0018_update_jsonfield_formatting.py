# Generated by Django 2.2.11 on 2020-04-13 16:20

import collections
from django.db import migrations
import enterprise_catalog.apps.catalog.constants
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_create_catalog_learner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogquery',
            name='content_filter',
            field=jsonfield.fields.JSONField(default=dict, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'indent': 4, 'separators': (',', ':')}, help_text="Query parameters which will be used to filter the discovery service's search/all endpoint results, specified as a JSON object.", load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
        migrations.AlterField(
            model_name='contentmetadata',
            name='json_metadata',
            field=jsonfield.fields.JSONField(blank=True, default={}, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'indent': 4, 'separators': (',', ':')}, help_text="The metadata about a particular piece content as retrieved from the discovery service's search/all endpoint results, specified as a JSON object.", load_kwargs={'object_pairs_hook': collections.OrderedDict}, null=True),
        ),
        migrations.AlterField(
            model_name='enterprisecatalog',
            name='enabled_course_modes',
            field=jsonfield.fields.JSONField(default=enterprise_catalog.apps.catalog.constants.json_serialized_course_modes, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'indent': 4, 'separators': (',', ':')}, help_text='Ordered list of enrollment modes which can be displayed to learners for course runs in this catalog.', load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
        migrations.AlterField(
            model_name='historicalcontentmetadata',
            name='json_metadata',
            field=jsonfield.fields.JSONField(blank=True, default={}, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'indent': 4, 'separators': (',', ':')}, help_text="The metadata about a particular piece content as retrieved from the discovery service's search/all endpoint results, specified as a JSON object.", load_kwargs={'object_pairs_hook': collections.OrderedDict}, null=True),
        ),
        migrations.AlterField(
            model_name='historicalenterprisecatalog',
            name='enabled_course_modes',
            field=jsonfield.fields.JSONField(default=enterprise_catalog.apps.catalog.constants.json_serialized_course_modes, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'indent': 4, 'separators': (',', ':')}, help_text='Ordered list of enrollment modes which can be displayed to learners for course runs in this catalog.', load_kwargs={'object_pairs_hook': collections.OrderedDict}),
        ),
    ]
