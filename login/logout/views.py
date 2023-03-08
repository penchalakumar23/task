from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import viewsets, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authtoken.models import Token
from .models import User
from .serializer import Userserializer
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.




class UserViewset(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Userserializer
    queryset = User.objects.all()
    def post(self,request):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
    @api_view(["POST"])
    def login(self,request):
        username=request.data.get('name')
        password=request.data.get('password')
        if username is None or password is None:
            return Response({'error':'please provide both username and password'},status=HTTP_400_BAD_REQUEST)
        user=authenticate(name=username,password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},
                        status=HTTP_200_OK)
