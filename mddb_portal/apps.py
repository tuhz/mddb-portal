import os
# from django.conf import settings
from django.apps import AppConfig

from mddb_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class MDDBIndexConfig(AppConfig):
    name = 'mddb_portal'


SEARCH_INDEXES = {
    'mddb': {
        # 'uuid': '808dc518-511a-4de0-af6f-fcf41da4767b',
        'uuid': 'f81ff04c-38c9-4a39-8eab-52329fb009b2',
        'name': 'MDDB Index',
        'group': 'f08083f3-db94-11ec-9616-51db4d10f5bd',
        'base_templates': 'globus-portal-framework/v2/',
        'tabbed_project': False,
        'access': 'private',
        'template_override_dir': 'mddb',
        'description': (
            'MDDB provides information on symmetry/phase labels (SPL), '
            'sample descriptors (DSC), material properties (PRO), '
            'material applications (APL), synthesis methods (SMT), '
            'and characterization methods (CMT) for inorganic materials'
        ),
        'fields': [
            ('title', fields.title),
            # 'material',
            'descriptor',
            # 'value',
            # ('material', fields.material),
            # ('descriptor', fields.descriptor),
            # ('value', fields.value),
            # ('reference', fields.reference),
            # ('globus_app_link', fields.globus_app_link),
            # 'dc',
            # ('copy_to_clipboard_link', fields.https_url),
            ('search_results', fields.search_results),
        ],
        'facets': [
            {
                "name": "Descriptor",
                "field_name": "descriptor",
            },
            # {
            #     "name": "Descriptor",
            #     "field_name": "dc.creators.creatorName",

            # },
            # {
            #     "name": "Dates",
            #     "field_name": "dc.dates.date",
            #     "type": "date_histogram",
            #     "date_interval": "day",
            # },
        ]
    }
}
