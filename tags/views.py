from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import WritetagSerializer, ReadTagSerializer
from django.utils.text import slugify
from tags.models import Tag
from rest_framework import status
# Create your views here.


'''
Use Case - 1
One use case of serializer is to validate date from client side and write into database where Serializer(data=request.data)

Use case - 2
Second use case of serializer is to convert orm object into json data 
Serializer(instance=object)


'''

class CreateTagView(APIView):


    def post(self, request):
        # IMPORTANT!!!
        #Use case -1
        #For write operation we use data=request.data
        serializer =  WritetagSerializer(data=request.data)
        if serializer.is_valid():
            #if serializer is valid we are creating the tag
            name = serializer.validated_data.get('name')
            tag_object = Tag.objects.create(
                name = name,
                slug = slugify(name)
            )
            #IMPORTANT !!!!
            #Use case - 2
            # For read operation we use instance=object to convert orm data into json data
            json_data = ReadTagSerializer(instance=tag_object).data
            return Response(data=json_data, status=status.HTTP_201_CREATED)
        else:
            #we are returning the error message
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class DetailTagView(APIView):

    def get(self, request, slug):
        try:
            tag_object = Tag.objects.get(slug=slug)
            json_data = ReadTagSerializer(instance=tag_object).data
            return Response(json_data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist as e:
            return Response({"message": "Tag does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned as e :
            return Response({"message": "Multiple tags are available"}, status=status.HTTP_400_BAD_REQUEST)
        
    

