from rest_framework import serializers
from tags.models import Tag

#serializer is used for data validation & Tag creation
#write operation into the database
class WritetagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


#serializer used to convert orm into json data
#read operation from the database
class ReadTagSerializer(serializers.ModelSerializer):

    #Formating some fileds which are present in the models

    created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created_at']