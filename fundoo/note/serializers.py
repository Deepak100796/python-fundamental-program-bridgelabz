from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes, Label
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import NotesDocument


class NotesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = NotesDocument
        fields = [
            'note'
        ]


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']


class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class NotesSerializer(serializers.ModelSerializer):
    label = LabelSerializer(many=True, read_only=True)
    collaborators = CollaboratorsSerializer(many=True, read_only=True)
    class Meta:
        model = Notes
        fields = ['title', 'note', 'label', 'url', 'is_archive', 'collaborators', 'image', 'reminder', 'color']


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title', 'note']


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['title', 'note', 'label', 'url', 'is_archive', 'collaborators'
            , "is_copied", 'checkbox', 'is_pined', 'is_trashed', 'color', 'reminder']