from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import User
from rest_framework import status
from django.contrib.auth.models import auth
from authentication.serializer import ReadUserSerializer
from authentication.permissions import IsUserActive
from rest_framework.pagination import PageNumberPagination
# Create your views here.


class SignupView(APIView):

    authentication_classes = []
    permission_classes = []
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        if not username:
            return Response({"error": "Enter a valid username"}, status=status.HTTP_401_UNAUTHORIZED)
        if not email:
            return Response({"error": "Enter a valid email"}, status=status.HTTP_401_UNAUTHORIZED)
        if not password:
            return Response({"error": "Enter a valid password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        if User.objects.filter(username=username):
            return Response({"error": "Enter a different username"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email):
            return Response({"error": "Enter a different email"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(password=password):
            return Response({"error": "Enter a different password"}, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user = auth.authenticate(username=username, password=password)
        if user:
            return Response({"success": True, "message": "Successfully Authenticated"}, status=status.HTTP_200_OK)
        else:
            return Response({"success": False, "message": "Unauthenticated"}, status=status.HTTP_400_BAD_REQUEST)
        
class LargePaginateResponse(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class UserListView(APIView):
    permission_classes = [IsUserActive, ]
    
    def get(self, request):
        queryset = User.objects.all()
        paginate_class = LargePaginateResponse()
        paginate_queryset = paginate_class.paginate_queryset(queryset=queryset, request=request)
        serializer_data = ReadUserSerializer(instance=paginate_queryset, many=True)
        paginate_response = paginate_class.get_paginated_response(data=serializer_data.data)
        paginate_response =True
        return paginate_response

