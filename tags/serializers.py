from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):

    #Formating some fileds which are present in the models

    created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at']