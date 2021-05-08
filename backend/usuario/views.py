from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

# Create your views here.
class UserRegistrationAPIView(APIView):
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            new_user = serializer.save()
            data['username'] = new_user.username
            data['email'] = new_user.email
        else:
            data = serializer.errors
        
        return Response(data=data)
