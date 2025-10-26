from rest_framework import serializers
from books.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=200)
    subtitle = serializers.CharField(required=False, allow_blank=True, max_length=200)
    author = serializers.CharField(required=True)
    isbn = serializers.CharField(required=True, max_length=13, min_length=10)
    
    def create(self, validated_data):
        """
        Create and retuen a new Book instance, given the validated data.
        """
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an exiting Book instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.subtitle = validated_data.get('subtitle', instance.subtitle)
        instance.author = validated_data.get('author', instance.author)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()

        return instance