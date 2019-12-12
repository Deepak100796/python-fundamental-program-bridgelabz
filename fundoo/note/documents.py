from elasticsearch_dsl import connections
#
connections.create_connection(hosts=['localhost'], timeout=20)
from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document
from .models import Notes, Label
from django_elasticsearch_dsl.registries import registry

from django.conf import settings

from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField
from django_elasticsearch_dsl_drf.analyzers import edge_ngram_completion

from elasticsearch_dsl import analyzer, tokenizer

html_strip = analyzer(
    'html_strip',
    tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=3),
    filter=["lowercase", "stop", "snowball"]
)


@registry.register_document
class NotesDocument(Document):
    note = fields.TextField(
        analyzer=html_strip
    )
    title = fields.TextField(
        analyzer=html_strip
    )
    color = fields.TextField(
        analyzer=html_strip
    )
    user = fields.ObjectField(properties={
        'email': fields.TextField(analyzer=html_strip),
        'username': fields.TextField(),
    })
    label = fields.ObjectField(properties={
        'name': fields.TextField(analyzer=html_strip),

    })
    reminder = fields.TextField(
        analyzer=html_strip
    )

    class Index:
        # Name of the Elasticsearch index
        name = 'note'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Notes # The model associated with this Document