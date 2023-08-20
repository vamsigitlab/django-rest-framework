from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from authentication.models import User
from rest_framework import status
from django.contrib.auth.models import auth
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
        