from rest_framework import serializers
from .models import User,File


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    conferm_password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        return User.objects.create(**validated_data)

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         field = ('id', 'image_path' , 'order' , 'version')

# from rest_framework import serializers


# class MyFileSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = MyFile
#         fields = ('file', 'description', 'uploaded_at')

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')