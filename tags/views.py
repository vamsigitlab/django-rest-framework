from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import WritetagSerializer, ReadTagSerializer
from django.utils.text import slugify
from tags.models import Tag
from rest_framework import status
from django.core.cache import cache
from rest_framework.generics import RetrieveAPIView, ListAPIView
from tags.filters import StandardResultsSetPagination
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
            cache_key = f"tag-{slug}"
            cached_data = cache.get(cache_key)
            if cached_data:
                print("comming from the cache")
                return Response(cached_data, status=status.HTTP_200_OK)
            else:
                tag_object = Tag.objects.get(slug=slug)
                json_data = ReadTagSerializer(instance=tag_object).data
                cache.set(cache_key, json_data)
                print("generated the data and caching the data")
                return Response(json_data, status=status.HTTP_200_OK)
        except Tag.DoesNotExist as e:
            return Response({"message": "Tag does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Tag.MultipleObjectsReturned as e :
            return Response({"message": "Multiple tags are available"}, status=status.HTTP_400_BAD_REQUEST)
        
    

#Write Operations
#Read operations
#High number of write operations like update, modify etc in this it's not good to implement the cache
#High number of read operations in this case we can implement the cache


class ListTagView(APIView):

    def get(self, request):
        try:
            query_set = Tag.objects.all()
            response_data = ReadTagSerializer(instance=query_set, many=True).data
            return Response(data=response_data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Unable to fetch the tags list"}, status=status.HTTP_400_BAD_REQUEST)
        

#Generic View ----> RetrieveAPIView, ListAPIView

class DetailTagV2View(RetrieveAPIView):
    print("Inside the Retrive API view")
    queryset = Tag.objects.all()
    serializer_class = ReadTagSerializer
    lookup_field = "slug"



class ListTagV2View(ListAPIView):
    print("Inside the List API view")
    queryset = Tag.objects.all()
    serializer_class = ReadTagSerializer
    pagination_class = StandardResultsSetPagination



class DeleteTagView(APIView):

    def post(self, request, slug):
        try:
            tag_object = Tag.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message": f"Deleted the tag with slug {slug}"}, status=status.HTTP_200_OK)
        except Tag.DoesNotExist as e:
            return Response({"message": "Unable to delete"}, status=status.HTTP_400_BAD_REQUEST)